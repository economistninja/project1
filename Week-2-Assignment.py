# Create an empty list called my_list.
# Append the following elements to my_list: 10, 20, 30, 40.
# Insert the value 15 at the second position in the list.
# Extend my_list with another list: [50, 60, 70].
# Remove the last element from my_list.
# Sort my_list in ascending order.
# Find and print the index of the value 30 in my_list. -->

# Create an empty list called my_list
my_list = []

# Append the elements: 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(f"After appending 10, 20, 30, 40: {my_list}")

# Insert the value 15 at the second position (index 1) in the list
my_list.insert(1, 15)
print(f"After inserting 15 at index 1: {my_list}")

# Extend my_list with another list: [50, 60, 70]
my_list.extend([50, 60, 70])
print(f"After extending with [50, 60, 70]: {my_list}")

# Remove the last element from my_list
my_list.pop() # .pop() without an argument removes the last element
print(f"After removing the last element: {my_list}")

# Sort my_list in ascending order
my_list.sort()
print(f"After sorting in ascending order: {my_list}")

# Find and print the index of the value 30 in my_list
index_of_30 = my_list.index(30)
print(f"The index of value 30 is: {index_of_30}")
