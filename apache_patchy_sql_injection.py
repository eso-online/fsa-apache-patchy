#! /usr/bin/python3

import os, sys, subprocess, fileinput

#Check to see if user ran with sudo
if os.geteuid() == 0:
    print("We're root!")
else:
    print("We're not root.")
    subprocess.call(['sudo', 'python3', *sys.argv])
    sys.exit()

# Install ModSecurity
print("Installing ModSecurity...\n")
os.system('apt-get install libapache2-mod-security2 -y')

# Remove the .recommended extension from the ModSecurity configuration file name
os.system('cp /etc/modsecurity/modsecurity.conf-recommended /etc/modsecurity/modsecurity.conf')

# Restart Apache server
os.system('sudo service apache2 reload')

# Modify /etc/modsecurity/modsecurity.conf
# Define the path to the ModSecurity conf file
conf_file_path = '/etc/modsecurity/modsecurity.conf'

print("ModSecurity Installed\n")

# Update configuration file with 'SecRuleEngine On'
print("Updating configuration files...\n")
with fileinput.FileInput(conf_file_path, inplace=True) as file:
    for line in file:
        # Replace "SecRuleEngine DetectionOnly" with "SecRuleEngine On"
        print(line.replace('SecRuleEngine DetectionOnly', 'SecRuleEngine On'), end='')
            
# Modify /etc/apache2/mods-available/security2.conf
# Define the path to the Apache2 conf file
conf_file_path = '/etc/apache2/mods-available/security2.conf'

# Define the text to be inserted
new_line = '\t#Include to modsecurity for SQL Injection Prevention'

# Use fileinput to modify the conf file in-place
with fileinput.FileInput(conf_file_path, inplace=True) as file:
    for line in file:
        if line.startswith('</IfModule>'):
            print(new_line)
        print(line.rstrip())

# Define the text to be inserted
new_line = '\tIncludeOptional "/usr/share/modsecurity-crs/*.conf"'

# Use fileinput to modify the conf file in-place
with fileinput.FileInput(conf_file_path, inplace=True) as file:
    for line in file:
        if line.startswith('</IfModule>'):
            print(new_line)
        print(line.rstrip())

# Define the text to be inserted
new_line = '\tIncludeOptional "/usr/share/modsecurity-crs/activated_rules/*.conf"'

# Use fileinput to modify the conf file in-place
with fileinput.FileInput(conf_file_path, inplace=True) as file:
    for line in file:
        if line.startswith('</IfModule>'):
            print(new_line)
        print(line.rstrip())

print("Configuration complete.\n")
