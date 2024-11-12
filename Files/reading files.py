employee_file = open("employees.txt", "r")       # modes- r-read, w-write, a-append, r+-read & write

print(employee_file.readable())        # Checking if the file is readble
print(employee_file.read())            # Reading the contents inside a file
print(employee_file.readline())        # Reading an individual line in a file
print(employee_file.readlines())      # Read all lines in the file and put them in an array
print(employee_file.readlines()[1])   # Accesing a specific line inside the array of lines

for employee in employee_file.readlines():    # Print all info in a file
    print(employee)


employee_file.close()        # Closing the file. it is recommended to close a file after openning

