employee_file = open("employees.txt", "a")    # a - appending. Adding to the file, w - will overwrite everything on the file

employee_file = open("employees1.txt", "w")    # creating a new file

# employee_file.write("Toby - Human Resources")
employee_file.write("\nKelly - Customer Service")  # To add on a new line



employee_file.close
