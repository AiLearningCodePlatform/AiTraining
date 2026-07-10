# variables( should start with character or _) & data types

# 2 types of variables
# local  #initialized with in loop/function/class
# & gloabal variables initialized & kept top of the code

inputint_value = 1
print(type(inputint_value))  # to check the data type
inputfloat_value = 9.0
print(type(inputfloat_value))
inputstr_value = "learning python"
print(type(inputstr_value))

# when we write coding
# 1 importing the modules
# 2 variables
# 3 loop/function/class/condition
# 4 executing the function or loop


def f1():
    inpintlocal_value = 10
    print("inside funtion", inputint_value)


f1()
