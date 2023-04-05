#! /usr/bin/python3 
import subprocess

# Update the package list
subprocess.call(['sudo', 'apt-get', 'update'])

# Upgrade the Apache package
subprocess.call(['sudo', 'apt-get', 'install', '--only-upgrade', 'apache2'])
