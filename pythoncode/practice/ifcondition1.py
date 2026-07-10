a = 5
b = 10

if a > b:
    print("a is greater than b")
elif b > a:
    print("b is greater than a")
else:
    print("a & b are equal")

import shutil

total, used, free = shutil.disk_usage("/")
usage = used / total * 100
if usage > 80:
    print("disk usage is above 80%")
else:
    print("disk usage is less 80%")

import os

serverip = ["1.1.1.1", "8.8.8.8", "127.0.0.1"]
# both for loop & if condition

for i in serverip:
    if os.system("ping -c 1" + i) == 0:
        print(f"server {i} is reachable")
    else:
        print(f"server {i} is not reachable")

# what are ports opens in my laptop & check whether port 80 is open or not
# check the cpu utilization of system if cpu utilization is more then 80% print warning message else print normal message
