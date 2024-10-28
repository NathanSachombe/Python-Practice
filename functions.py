# 1. Function basics
    # - Collection of code that performs a specific task
    # - function name should be all lower case & seperated by underscore if more than two words


def sayhi():             # Define the function
    print("Hello User")

sayhi()                 # Calling the function

def say_hi(name, age):                              # Function with parameters
    print("Hello " + name + ", you are " + str(age) + " years old")

say_hi("Willow", 25)
say_hi("Grace", 23) 


# 2. Return statement

def cube(num):
    return num*num*num


print(cube(3))





 