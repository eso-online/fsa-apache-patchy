#! /usr/bin/python3

import os, sys, subprocess

if os.geteuid() == 0:
    print("We're root!")
    os.system('sudo /etc/init.d/apache2 stop')
    print("Stopping Apache2 Server")
    os.system('sudo a2enmod headers')
    print("Enabling Headers")  
else:
    print("We're not root.")
    subprocess.call(['sudo', 'python3', *sys.argv])
    sys.exit()



content = '''\
Header set X-XSS-Protection "1; mode=block"
Header set Strict-Transport-Security "max-age=31536000; includeSubDomains; preload"
Header set Content-Security-Policy "default-src 'self'; font-src *;img-src * data:; script-src *; style-src *;"
Header set X-Frame-Options "SAMEORIGIN"
Header set X-Content-Type-Options "nosniff"
Header set Referrer-Policy "strict-origin"
Header set Permissions-Policy "geolocation=(),midi=(),sync-xhr=(),microphone=(),camera=(),magnetometer=(),gyroscope=(),fullscreen=(self),payment=()"
TraceEnable off
'''

with open('/etc/apache2/apache2.conf', 'a') as f:
    f.write(content) 
    print("XSS Patches Applied!")

os.system('sudo /etc/init.d/apache2 restart') 
print("Apache2 reloading")
#os.system('sudo systemctl status apache2')
