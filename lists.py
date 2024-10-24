# 1. Lists basics

friends = ["Alex", "Gabriel", "Nancy", "Grace", "Jane", "Ashley", "Alex"] # Making a list. We use square brackets
lucky_numbers = [4, 38, 15, 16, 23, 15]
fruits = ["apple", "banana", "orange"]

#print(friends[0]) # Accessing a specific element in the list using index
#print(friends[-1]) # Accessing a specific element in the list using index from the last position
#print(friends[1:3]) # Accessing elements in a range

#friends[1] = "Pauline" # Modifying elemets in a list
#print(friends)

# 2. List functions

friends.extend(fruits) # Add two lists together
print(friends)

friends.append("Fatuma") # Add an element to the end of the list
print(friends)

friends.insert(1, "Fatuma") # Add an element to the list at a specific position
print(friends)

friends.remove("Nancy") # Remove an element from the list
print(friends)

fruits.clear() # Remove all elements in the list
print(fruits)

friends.pop() # Remove the last element on the list
print(friends)

print(friends.index("Grace")) # To get the specific position of an element in a list

print(friends.count("Alex")) # To count the number of times an element appears in a list

friends.sort() # Sort the list in ascending order
print(friends)

lucky_numbers.sort()
print(lucky_numbers)

friends.reverse() # Sort the list in descending order
print(friends)

lucky_numbers.reverse() # Sort the list in descending order
print(lucky_numbers)

friends2 = friends.copy() # Copy all elements in a list and create a new list
print(friends2)







 