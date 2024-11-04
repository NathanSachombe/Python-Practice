# For catching errors

try:
    # value = 10/0         # To show the broadbased approach of the except block
    number = int(input("Enter a number: "))
    print(number)
except ValueError:
    print("Invalid input")