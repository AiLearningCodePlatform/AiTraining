"""import os
from dotenv import load_dotenv #env variables from .env file will be loaded using python-dotenv package

load_dotenv()
key=os.getenv("APK_KEY")

print(key)"""

# if condition:
# activity
# elif condition:
# activity
# else:
# activity

'''a = 15
if a < 10:
    print("a is less than 10")
else:
    print("a is greater than 10")'''
'''import shutil

total, used, free = shutil.disk_usage("C:\\")

print("Total:", total/(2**30), "GB")
print("Used:", used/(2**30), "GB")
print("Free:", free/(2**30), "GB")'''

'''import socket # module to work with sockets, used to check port status

def check_port(port): # function to check if a port is open or closed
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a TCP connection over IPv4
    result = s.connect_ex(("127.0.0.1", port))
    if result == 0:
        print(f"Port {port} is OPEN")
    else:
        print(f"Port {port} is CLOSED")
    s.close()

check_port(135)'''

import psutil

cpu_usage = psutil.cpu_percent(interval=1)
print(f"CPU Usage: {cpu_usage}%")