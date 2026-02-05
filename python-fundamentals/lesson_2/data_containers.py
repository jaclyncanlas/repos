# working with data containers in Python

# container - a data structure that helps model reality

# lists
print("LISTS\n")

temperatures = [21.5, 22.0, 23.1, 35.2, 5.4]
print("first temperature:", temperatures[0])
print("last temperature:", temperatures[-1])

# slicing - to access a specific subset of the list
print(temperatures[0:2])  # from index 0 to (but not including) index 2
print(temperatures[1:])   # from index 1 to the end
print(temperatures[:3])   # from the start to (but not including) index
# slicing allows out-of-bounds without error
# slicing allows negative indexing

# append() - adds an element to the end of the list
temperatures.append(19.8)
print("after appending 19.8:", temperatures)

# iteration - loops through each element in the list
for temp in temperatures:
    print("temperature:", temp)

# enumerate() - gets the index and the value at index in list
for index, temp in enumerate(temperatures):
    print(f"temperature at index {index} is {temp}")

# AVOID AT ALL COSTS: 
# for i in range(len(temperatures)):  # avoid unless necessary
    #     print(f"temperature at index {i} is {temperatures[i]}")

# strings
print("\nSTRINGS")

name = "Jaclyn"

# indexing - access specific character in string
print("indexing")
print(name[0])
print(name[-1])

# iteration - loops through each character in the string
for char in name:
    print("iteration | character:", char)

# slicing - access a specific subset of the string
print("slicing | ", name[0:3])  # from index 0 to (but not including) index 3

# immutability - string values cannot be changed
# name[0] = "j"  # this would raise an error

# dictionaries
# maps key-> value pairs
print("\nDICTIONARIES\n")
student = {
    "name": "Jaclyn",
    "program": "Intergrated engineering",
    "year standing": 4,
    "year graduating": 2026
}

# accessing values by key
print("name:", student["name"])

# safely accessing values by key using get()
print("program:", student.get("program"))

# get() - if key is missing, assign fallback value
print("age:", student.get("age:", "not specified"))

# update dictionary with key value pair
student["year"] = 6
student["graduated"] = False
print("updated student dictionary:", student)

# sets
print("\nSETS\n")

# set: unordered collection of UNIQUE elements
courses = {"ELEC 344", "ELEC 413", "ELEC 221", "ELEC 331"}

# membership
print("is ELEC 221 part of courses?", "ELEC 221" in courses)

# uniqueness
numbers = [1, 2, 3, 4, 2, 5, 6, 7, 1, 2]
unique_numbers = set(numbers)
print("unique numbers:", unique_numbers)

# set as a function- can this work with other data types? update: yes
full_name = "Jaclyn Canlas"
unique_characters = set(full_name)
print("unique characters in full name:", unique_characters)

# Nested structures
print("\nNESTED STRUCTURES\n")

expenses = [{"category": "food", "amount": 25.50},
            {"category": "transportation", "amount": 15.75},
            {"category": "entertainment", "amount": 40.00},
            {"category": "food", "amount": 45.00},]

# iterate
# e is a dict
for e in expenses:
    print(e.get("category"), e.get("amount"))

# accumulate total expenses
total_expenses = 0.0
for e in expenses:
    total_expenses += e.get("amount", 0.0)
print("total expenses:", total_expenses)