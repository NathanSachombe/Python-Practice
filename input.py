# 1. Getting input from users

name = input("Enter your name: ")
age = input("Enter your age: ")

print("Hello " + name + "! You are " + age + " years old.")

# 2. Building a basic calculator

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = int(num1) + int(num2) # You have to convert the input to numbers coz it will be in string
result_decimal = float(num1) + float(num2) # Use this if the input has decimal values

print(result)

# 3. Building a madlibs game

color = input("Enter a color: ")
plural_noun = input("Enter a plural noun: ")
celebrity = input("Enter a celebrity: ")

print("Roses are " + color)
print(plural_noun + " are blue")
print("I love " + celebrity)




