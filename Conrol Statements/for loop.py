# Iterate through something

for letter in "Giraffe Academy":        # Loop through a string
    print(letter)

friends = ["Sandra", "Karen", "Zoe"]     # Loop through an array
for friend in friends:
    print(friend)

for index in range(10): # all numbers from 0 to 10 but not including 10
    print(index)

for index in range(2, 5): # numbers between 2 and 5 but not including 5
    print(index)

for index in range(5):
    if index == 0:
        print("First iteration")
    else:
        print("Not first")


# Exponent function using for loop(Raise to power)
def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(3, 4))



