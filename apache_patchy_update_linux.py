import os

# Check if user has root privileges
if os.geteuid() == 0:
    print("We're root!")
else:
    print("We're not root.")
    subprocess.call(['sudo', 'python3', *sys.argv])
    sys.exit()

# Update package lists
os.system("apt-get update -y")

# Upgrade packages
os.system("apt-get upgrade -y")

# Clean up packages
os.system("apt-get autoremove -y")
