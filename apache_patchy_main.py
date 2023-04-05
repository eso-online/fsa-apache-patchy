#! /usr/bin/python3

import os, subprocess, sys

if os.geteuid() == 0:
    print("We're root!")
else:
    print("We're not root.")
    subprocess.call(['sudo', 'python3', *sys.argv])
    sys.exit()

os.system("chmod +x apache_patchy_update_linux.py")
os.system("chmod +x apache_patchy_xss_protection.py")
os.system("chmod +x apache_patchy_sql_injection.py")
os.system("chmod +x apache_patchy_info_leakage.py")
os.system("chmod +x apache_patchy_session_management.py")

while True:
    print("  ____  ____   ____    __  __ __    ___ \n /    ||    \ /    |  /  ]|  |  |  /  _]\n|  o  ||  o  )  o  | /  / |  |  | /  [_ \n|     ||   _/|     |/  /  |  _  ||    _]\n|  _  ||  |  |  _  /   \_ |  |  ||   [_ \n|  |  ||  |  |  |  \     ||  |  ||     |\n|__|__||__|  |__|__|\____||__|__||_____|\n                                        \n ____   ____  ______   __  __ __  __ __ \n|    \ /    ||      | /  ]|  |  ||  |  |\n|  o  )  o  ||      |/  / |  |  ||  |  |\n|   _/|     ||_|  |_/  /  |  _  ||  ~  |\n|  |  |  _  |  |  |/   \_ |  |  ||___, |\n|  |  |  |  |  |  |\     ||  |  ||     |\n|__|  |__|__|  |__| \____||__|__||____/ \n\n")

    print("Welcome to Table 4's Apache Patchy.\nPlease select an option:")
    print("1. Update Linux")
    print("2. Run XSS Protection script")
    print("3. Run SQL Injection Protection script")
    print("4. Run Info Leakage Protection script")
    print("5. Run Session Management Protection script")
    print("6. Run all scripts")
    print("7. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        os.system("python3 apache_patchy_update_linux.py")
    elif choice == '2':
        os.system("python3 apache_patchy_xss_protection.py")
    elif choice == '3':
        os.system("python3 apache_patchy_sql_injection.py")
    elif choice == '4':
        os.system("python3 apache_patchy_info_leakage.py")
    elif choice == '5':
        os.system("python3 apache_patchy_session_management.py")
    elif choice == '6':
        os.system("python3 apache_patchy_update_linux.py && python3 apache_patchy_xss_protection.py && python3 apache_patchy_sql_injection.py && python3 apache_patchy_info_leakage.py && python3 apache_patchy_session_management.py")
    elif choice == 'd':
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀⢤⡤⡤⢤⢤⢤⠤⠄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠴⠂⠉⠁⣀⢠⡊⠀⠀⠀⠀⢈⢻⣄⣀⣈⣉⣐⠢⠄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠊⠉⠁⠀⠀⠂⠄⠀⠀⠀⠀⠀⠀⠀⠀⠠⣶⠔⡎⢒⠶⣄⠀⠉⡑⢦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⣠⠾⠉⠀⠀⠀⠀⡀⠠⠆⠀⠀⠀⠀⠀⠀⠀⠘⠀⠀⢾⣆⡘⢷⡸⠢⠲⡀⢑⠄⠉⠳⣄⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⣠⠞⠁⣀⣀⣠⠄⠀⡌⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣏⣳⡘⣯⡘⣧⠰⡆⠙⡔⠬⠾⣷⣄⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⡔⢃⠔⣋⠤⠀⠐⠽⡞⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⡿⣌⡇⠸⣇⠘⣷⠘⣧⡘⢮⢻⣝⣎⢧⡀⠀⠀⠀\n⠀⠀⢀⠞⡴⢡⠞⠡⠀⠀⠀⠀⢹⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⢠⡏⣷⡁⢙⣆⢹⣷⡘⣧⣨⣯⣿⣽⣯⣷⡀⠀⠀\n⠀⠀⡞⡜⡰⠉⢲⣄⡣⣔⣢⡄⠸⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣲⡀⠜⣏⣁⢉⣺⣶⢒⣫⡼⣾⡥⡾⠻⣿⣿⣿⣷⡀⠀\n⠀⡼⣴⠀⠀⠀⠀⠑⡞⠁⠈⡇⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⡞⡇⣳⣿⠁⠨⣿⢿⠈⠛⢫⢹⢏⣧⣤⣿⣷⣿⣿⣷⠀\n⢠⢣⠀⠀⠀⠀⠀⢸⡀⠀⡜⠉⠀⠀⠄⠀⠀⠀⠀⠀⠠⠄⠠⠀⠃⠄⠇⠷⠟⠷⡽⠼⡞⣻⢷⣱⣿⣿⢺⣿⣿⣿⣿⣿⣿⣿⡄\n⣼⣼⠀⠀⠀⠀⠀⠀⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡂⢰⠸⢼⢹⠄⠁⠆⢨⠧⠀⢺⢸⠘⡿⠉⣻⡏⣿⣿⣿⢿⣿⣿⣿⣧\n⡿⠠⡆⠀⢄⡀⠀⢀⡠⡦⠂⠀⠀⠀⢐⠀⠀⠀⠀⢠⢸⠀⢸⢸⢸⠀⠀⠐⢶⣿⡃⠀⠠⠘⡇⣧⣾⣿⣇⣿⣿⣿⣾⣿⣿⣿⣿\n⡇⣀⡆⣄⠀⠈⠉⢑⠃⢈⠀⠀⠀⠀⢸⠆⠀⣀⠀⠀⢐⠌⢲⢸⠸⠋⠀⢀⢾⣬⡗⢶⣠⡲⡇⣿⣿⣿⣿⢸⣿⣿⡇⣿⣿⣿⣿\n⣿⢭⡁⠈⠉⠀⠀⢐⠀⠐⠀⠀⠀⠀⢸⡀⠀⠀⠀⢠⢸⡅⠘⢸⠨⠁⠀⠰⡙⢹⢧⡾⣻⣿⡇⢸⣿⣿⣿⢸⣿⡿⠟⠟⣋⣭⣿\n⢸⣶⣬⣝⡒⠦⢤⣤⣄⣁⣀⠀⠀⠀⠘⠋⠈⠘⠛⠲⠸⠲⠞⠺⠸⠿⠦⠳⠓⠙⠘⠛⠛⠛⠃⠘⣋⣉⣩⣤⣤⡴⠖⣛⣯⣿⡟\n⠈⡄⡿⠴⠄⣭⢃⢰⢰⢤⢬⡍⣍⡙⡛⣛⣛⡛⡓⠒⠒⠒⠒⠒⠒⠒⠐⠒⣛⣛⣛⣛⣛⣻⣯⣭⣭⣽⣶⣾⣿⣿⣿⣿⣿⣿⠃\n⠀⢻⣽⢮⢺⣋⠦⠙⡰⣏⡘⣪⡧⡦⣷⡊⢨⡇⡿⢏⣿⣧⡤⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀\n⠀⠀⢿⣾⡇⡾⡎⣐⡇⡷⡋⢹⣽⢟⡻⣯⣤⣼⣿⣷⢿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀\n⠀⠀⠈⢿⣿⣿⣷⡯⢿⣰⣆⡳⣿⣿⣿⣿⣷⣽⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀\n⠀⠀⠀⠀⠻⣿⣷⣿⣿⣏⣿⣿⣿⣿⣷⣿⣿⣿⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀\n⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠙⠛⠛⠛⠛⠛⠋⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n\n")
    elif choice == '7':
        break
    else:
        print("Invalid choice. Please try again.")
