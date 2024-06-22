use std::{io::{Read, Write}, path::Path, process::Command, sync::{Arc, Mutex}};

use rand::{Rng, SeedableRng};
use subprocess::{Popen, PopenConfig};

use crate::terminal::AsyncTerminal;

///
/// # Get Temporary Home
/// 
/// This function is used to retrieve the temporary home directory of a given username. The temporary home
/// directory is used to store temporary files for the user. The temporary home directory is located in the
/// `/tmp` directory.
/// 
fn create_home_temporary<P: AsRef<str>>(username: &P) -> Result<String, String> {
    let path = Path::new("/tmp/tmp_user_home").join(username.as_ref());

    // Create the parent folder of the path
    let parent = path.parent()
        .ok_or("Failed to get the parent folder of the path".to_string())?;

    std::fs::create_dir_all(parent)
        .map_err(|_| "Failed to create the parent folder of the temporary home directory")?;

    // Remove the existing folder
    if path.exists() {
        std::fs::remove_dir_all(&path)
            .map_err(|_| "Failed to remove the existing temporary home directory")?;
    }

    // Create the new folder
    std::fs::create_dir(&path)
        .map_err(|_| "Failed to create the temporary home directory")?;

    // Return the path
    path.canonicalize()
        .map_err(|e| format!("Failed to canonicalize the path: {}", e))?
        .to_str()
        .ok_or("Failed to convert the path to a valid utf-8 string".to_string())
        .map(|r| r.to_string())
}

/// 
/// # Change ownership of the home directory
/// 
/// This function is used to change the ownership of the home directory of a given username. The ownership
/// of the home directory is changed to the user with the provided user id.
/// 
/// # Arguments
/// 
/// * `uid` - The user id of the user to change the ownership of the home directory.
/// * `home` - The path to the home directory.
/// 
fn change_home_ownership<P: AsRef<str>>(uid: u32, home: &P) -> Result<(), std::io::Error> {
    std::os::unix::fs::chown(
        home.as_ref(),
        Some(uid),
        Some(uid)
    )
}

///
/// # Kill all processes of a user
/// 
/// This function is used to kill all processes of a given user. The function will return `Ok(())` if all
/// processes of the user were successfully killed. Otherwise, the function will return `Err(String)` with
/// an error message.
/// 
/// # Arguments
/// 
/// * `uid` - The user id of the user to kill all processes.
/// 
fn kill_user_processes(uid: u32) -> Result<(), String> {
    let output = Command::new("pkill")
        .args([
            "-u", &uid.to_string()
        ])
        .output()
        .map_err(|e| format!("Failed to execute the command `pkill`: {}", e))?;
    let return_code = output.status.code().unwrap_or(-1);

    //
    // According to the documentation of `pkill`, the return code can be:
    // 1 - One or more processes were matched.
    // 2 - No processes were matched.
    // 3 - An syntax error occurred.
    // 4 - An fatal error occurred.
    //
    if return_code >= 0 && return_code <= 2 {
        Ok(())
    } else {
        Err(
            format!("Failed exit code: {} ({})",
                output.status.code().map(|r| r.to_string()).unwrap_or_else(|| "None".to_string()),
                String::from_utf8(output.stderr).unwrap_or_default()
            )
        )
    }
}

///
/// # User Id
/// 
/// In Unix-like operating systems, the user identifier (UID) is a unique positive integer assigned to each user.
/// This function is used to retrieve the user id of a given username. If the user does not exists, the function
/// will return `None`.
/// 
/// # Arguments
/// 
/// * `username` - The username of the user to retrieve the user id.
/// 
pub fn userid<P: AsRef<str>>(username: &P) -> Option<u32> {
    // Find the userid of the user with the provided username
    let output = Command::new("id")
        .args(["-u", username.as_ref()])
        .output()
        .expect("Failed to execute the command `id`");

    // Ensure the the exit is '0' (otherwise it is possible
    // the user don't exists)
    if output.status.success() {
        let str = String::from_utf8(output.stdout);
        str
            .inspect_err(|_| eprintln!("Failed to convert the result back to a valid utf-8 string"))
            .ok()
            .map(|r| r.lines().next().unwrap_or(&"").parse::<u32>().ok())
            .flatten()
    }
    else {
        None
    }
}

///
/// # User Add
/// 
/// This function is used to create a new user account with the provided username. If the user already exists,
/// the function will return the user id of the existing user. If the user account was successfully created,
/// the function will return the user id of the newly created user.
/// 
/// # Arguments
/// 
/// * `username` - The username of the user to create.
/// 
/// # Returns
/// 
/// The function will return the user id of the newly created user if the user account was successfully created.
/// 
pub fn useradd<P: AsRef<str>>(username: &P) -> Option<u32> {
    // Check that the user is not already existing
    if let Some(uid) = userid(username) {
        return Some(uid);
    }

    // Otherwise perform the request
    let output = Command::new("useradd")
        .args([
            username.as_ref()
        ])
        .output()
        .expect("Failed to execute the command `useradd`");

    // Finally, return the user id if the command was successful
    if output.status.success() {
        userid(username)
    }
    else {
        eprintln!("Failed to create the user account: {}", String::from_utf8(output.stderr).unwrap_or_default());
        None
    }
}


///
/// This structure is used to manage a pool of users. The pool will automatically create new users
/// when the pool is empty. The pool will also release the users back to the pool when they are no
/// longer needed.
/// 
pub struct UserPool {
    max_user: usize,
    user: Vec<(u32, String)>,
    available: Vec<(u32, String)>,
    random_state: rand_xorshift::XorShiftRng,
}

impl Default for UserPool {
    fn default() -> Self {
        let seed = [42; 16];
        Self {
            max_user: Self::DEFAULT_MAX_USER,
            random_state: rand_xorshift::XorShiftRng::from_seed(seed),
            user: Vec::with_capacity(Self::DEFAULT_MAX_USER),
            available: Vec::with_capacity(Self::DEFAULT_MAX_USER),
        }
    }
}

impl UserPool {
    pub const DEFAULT_MAX_USER: usize = 256;

    ///
    /// Create a new user pool with the provided maximum number of users.
    /// 
    /// # Arguments
    /// 
    /// * `max_user` - The maximum number of users in the pool.
    /// 
    pub fn new(max_user: usize) -> Self {
        Self {
            max_user: max_user,
            user: Vec::with_capacity(max_user),
            available: Vec::with_capacity(max_user),
            ..Default::default()
        }
    }

    fn next_user(&mut self) -> bool {
        assert!(self.user.len() <= self.max_user);

        let user = (&mut self.random_state)
            .sample_iter(rand::distributions::Alphanumeric)
            .take(8)
            .map(char::from)
            .collect::<String>();
        let user = format!("test_{}", user);

        if let Some(uid) = useradd(&user) {
            self.user.push((uid, user.clone()));
            self.available.push((uid, user));
            true
        }
        else {
            false
        }
    }

    fn get_user(&mut self) -> Option<(u32, String)> {
        if self.available.is_empty() {
            if !self.next_user() {
                return None;
            }
        }

        if self.user.len() == self.max_user {
            return None;
        }

        Some(self.available.pop().unwrap())
    }

    fn release_user(&mut self, user: u32) {
        if let Some(index) = self.user.iter().position(|(uid, _)| *uid == user) {
            let (_, username) = self.user.remove(index);
            self.available.push((user, username));
        }
    }

    pub fn alloc_user(this: Arc<Mutex<Self>>) -> Result<User, String> {
        let user = this.lock()
            .expect("☢️ Poisoned lock")
            .get_user();

        user.map(|(uid, username)| {
                // First we attempt to create the temporary home directory
                let home = create_home_temporary(&username)?;

                // Change the ownership of the home directory
                change_home_ownership(uid, &home)
                    .map_err(|e| format!("Failed to change the ownership of the home directory: {}", e))?;

                // Return the user account
                Ok(User {
                    uid,
                    username,
                    home,
                    pool: Some(this),
                })
            })
            .unwrap_or(Err("Failed to allocate a new user account".to_string()))
    }
}

///
/// Represents a user account in the pool. The user account will automatically be released back to the
/// pool when the user account is dropped.
/// 
pub struct User {
    uid: u32,
    username: String,
    home: String,
    pool: Option<Arc<Mutex<UserPool>>>,
}

impl Drop for User {
    fn drop(&mut self) {
        self.release();
    }
}

impl User {
    pub fn release(&mut self) {
        // Kill all processes of the user
        if let Err(e) = kill_user_processes(self.uid) {
            eprintln!("⚠️ Failed to kill all processes of the user: {}", e);
        }

        // Release the user account back to the pool
        if let Some(pool) = self.pool.take() {
            pool.lock()
                .expect("☢️ Poisoned lock")
                .release_user(self.uid);
        }
    }

    pub fn get_uid(&self) -> u32 {
        self.uid
    }

    pub fn get_username(&self) -> &str {
        self.username.as_str()
    }

    pub fn get_home(&self) -> &str {
        self.home.as_str()
    }

    pub fn spawn_terminal(this: Arc<Mutex<Self>>) -> Result<TerminalSession, String> {
        TerminalSession::new(this)
    }
}

///
/// This structure represent a unique terminal session for a user. The terminal session will automatically
/// create a new user account when the session is created. The terminal session will also release the user
/// account back to the pool when the session is dropped.
/// 
pub struct TerminalSession {
    _user: Arc<Mutex<User>>, // Used to protect against the user account being dropped
    process: Option<Popen>,
}

impl TerminalSession {
    ///
    /// Create a new terminal session for the provided user account.
    /// 
    /// # Arguments
    /// 
    /// * `user` - The user account to create the terminal session for.
    /// 
    /// # Returns
    /// 
    /// The function will return the terminal session if the session was successfully created.
    /// 
    pub fn new(user: Arc<Mutex<User>>) -> Result<Self, String> {
        // Retrieve the username and home directory
        let (username, home) = {
            let user = user.lock().expect("☢️ Poisoned lock");
            (user.get_username().to_string(), user.get_home().to_string())
        };


        // Create a new terminal session
        let shell_commands = format!("export HOME=\"{0}\"; cd \"{0}\"; exec /bin/bash", home);
        let popen = Popen::create(
            &[
                "su",
                "-s", "/bin/bash",
                "-P",
                "-c", &shell_commands,
                username.as_str()
            ],
            PopenConfig {
                stdout: subprocess::Redirection::Pipe,
                stderr: subprocess::Redirection::Pipe,
                stdin: subprocess::Redirection::Pipe,
                ..Default::default()
            }
        ).map_err(|e| format!("Failed to create the terminal session: {}", e))?;

        Ok(Self {
            _user: user,
            process: Some(popen),
        })
    }

    ///
    /// Close the terminal session. This will kill the terminal session and release the user account back
    /// to the pool.
    /// 
    pub fn close(&mut self) {
        if self.process.is_none() {
            return;
        }

        self.process.take().unwrap().kill().expect("Failed to kill the terminal session");
    }
}

impl Drop for TerminalSession {
    fn drop(&mut self) {
        self.close();
    }
}

impl AsyncTerminal for TerminalSession {
    fn write(&mut self, data: &[u8]) -> Result<(), String> {
        self.process.as_mut()
            .ok_or("The process is None".to_string())?
            .stdin
            .as_mut()
            .ok_or("Failed to get the stdin of the process".to_string())?
            .write_all(data)
            .map_err(|e| format!("Failed to write to the stdin of the process: {}", e))
    }

    fn read_stdout(&mut self, buffer: &mut [u8]) -> Result<usize, String> {
        self.process.as_mut()
            .ok_or("The process is None".to_string())?
            .stdout
            .as_mut()
            .ok_or("Failed to get the stdout of the process".to_string())?
            .read(buffer)
            .map_err(|_| std::string::String::from("Failed to read stdout"))
    }
    
    fn read_stderr(&mut self, buffer: &mut [u8]) -> Result<usize, String> {
        self.process.as_mut()
            .ok_or("The process is None".to_string())?
            .stderr
            .as_mut()
            .ok_or("Failed to get the stderr of the process".to_string())?
            .read(buffer)
            .map_err(|_| std::string::String::from("Failed to read stderr"))
    }
}


#[cfg(test)]
mod tests {
    use rand::Rng;

    use crate::pool::{useradd, userid};

    #[test]
    fn userid_work() {
        // Check that the root user exists with and UID of 0
        assert_eq!(userid(&"root"), Some(0));
        assert_eq!(userid(&"a_very_random_user_that_probably_wont_exists_0123456789"), None);
    }

    #[test]
    fn useradd_work() {
        let username: String = rand::thread_rng()
            .sample_iter(rand::distributions::Alphanumeric)
            .take(16)
            .map(char::from)
            .collect();
        let username = format!("test_{}", username);
        assert_eq!(useradd(&username).is_some(), true);
    }
}
