use std::{io::{Read, Write}, path::Path, process::Command, sync::{Arc, Mutex}};

use rand::{Rng, SeedableRng};

use crate::terminal::AsyncTerminal;

///
/// # Get Temporary Home
/// 
/// This function is used to retrieve the temporary home directory of a given username. The temporary home
/// directory is used to store temporary files for the user. The temporary home directory is located in the
/// `/tmp` directory.
/// 
fn create_home_temporary<P: AsRef<str>>(username: &P) -> Result<String, ()> {
    let path = Path::new("/tmp/tmp_user_home").join(username.as_ref());

    // Create the parent folder of the path
    std::fs::create_dir_all(path.parent().ok_or(())?)
        .expect("Failed to create the temporary home directory");

    // Remove the existing folder
    if path.exists() {
        std::fs::remove_dir_all(&path)
            .expect("Failed to remove the existing temporary home directory");
    }

    // Create the new folder
    std::fs::create_dir(&path)
        .expect("Failed to create the temporary home directory");

    // Return the path
    path.canonicalize()
        .map_err(|_| ())?
        .to_str()
        .ok_or(())
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
            max_user: 256,
            random_state: rand_xorshift::XorShiftRng::from_seed(seed),
            user: Vec::with_capacity(256),
            available: Vec::with_capacity(256),
        }
    }
}

impl UserPool {
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
            self.user.push((uid, user));
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

}

///
/// This structure represent a unique terminal session for a user. The terminal session will automatically
/// create a new user account when the session is created. The terminal session will also release the user
/// account back to the pool when the session is dropped.
/// 
pub struct TerminalSession {
    uid: u32,
    pool: Arc<Mutex<UserPool>>,
    process: Option<std::process::Child>,
    #[allow(dead_code)]
    home: String,
}

impl TerminalSession {
    pub fn new(pool: Arc<Mutex<UserPool>>) -> Result<Self, String> {
        let (uid, user) = {
            let mut pool = pool.lock().unwrap();
            pool.get_user().unwrap()
        };

        // Create the temporary home directory
        let home = create_home_temporary(&user)
            .map_err(|_| "Failed to create the temporary home directory")?;

        // Attempt to change the ownership of the home directory
        change_home_ownership(uid, &home)
            .map_err(|e| format!("Failed to change the ownership of the home directory: {}", e))?;

        // Create a new terminal session
        let process = Command::new("su")
            .args([
                "-s", "/bin/bash",
                "-P",
                "-c", "cd /; exec /bin/bash",
                user.as_str()
            ])
            .spawn()
            .expect("Failed to execute the command `su`");

        Ok(Self {
            uid,
            pool,
            process: Some(process),
            home: home,
        })
    }

    pub fn close(&mut self) {
        if self.process.is_none() {
            return;
        }

        self.process.take().unwrap().kill().expect("Failed to kill the terminal session");
        self.pool.lock().unwrap().release_user(self.uid);
    }
}

impl Drop for TerminalSession {
    fn drop(&mut self) {
        self.close();
    }
}

impl AsyncTerminal for TerminalSession {
    fn write(&mut self, data: &[u8]) -> Result<(), ()> {
        self.process.as_mut()
            .ok_or(())?
            .stdin
            .as_mut()
            .ok_or(())?
            .write_all(data)
            .map_err(|_| ())
    }

    fn read_stdout(&mut self, buffer: &mut [u8]) -> Result<usize, ()> {
        self.process.as_mut()
            .ok_or(())?
            .stdout
            .as_mut()
            .ok_or(())?
            .read(buffer)
            .map_err(|_| ())
    }

    fn read_stderr(&mut self, buffer: &mut [u8]) -> Result<usize, ()> {
        self.process.as_mut()
            .ok_or(())?
            .stderr
            .as_mut()
            .ok_or(())?
            .read(buffer)
            .map_err(|_| ())
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
