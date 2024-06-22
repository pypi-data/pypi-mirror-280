import vkernelrs as vk

# Create a pool with one user
pool = vk.PyUserPool()
print("PyUserPool created")

# Create a user
user = pool.allocate()
print(user)

# Create a new terminal session for the user
term = user.spawn()

# Virtual term
while True:
    output = term.read(4096).decode('utf-8', errors='replace')
    print(output, end='', flush=True)
    command = (input() + "\n").encode('utf-8')
    term.write(command)
    
    
