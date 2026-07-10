i = 8

oddnumber = []
evennumber = []

if i % 2 == 0:
    print(f"{i} is even")
    evennumber.append(i)
else:
    print(f"{i} is odd")
    oddnumber.append(i)

print("Even list:", evennumber)
print("Odd list:", oddnumber)