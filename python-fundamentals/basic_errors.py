# Practicing with common Python runtime errors
# Goal: Goal: Practice stack tracing and fixing errors in Python code

# IndexError practice
nums = [10, 20, 30]
print("len:", len(nums), "|", "nums:", nums)
#print(nums[3])
print(nums[2])

# This is an IndexError. It occurs on line 4 in the file bug3.py. Right before it crashes, we see that nums is trying to be accessed at index 3. I'll inspect state by printing out
# the length of the list. Here we can see that nums is a list with only 3 elements, so its index goes from 0 to 2. Therefore, to fix this, we should change the index we are trying to 
# access from 3 to 2. Then re-run it.

# NameError practice
name = "jaclyn"
#print(nam)
print(name)

# This is a NameError. It occurs on line 12 in the file bug3.py. Right before it crashes, we see that the code is trying to print the variable 'nam'. I'll inspect state by checking the variable
# assignment. However, in this code the variable 'nam' is not defined, and what is defined instead is 'name'. Thus, to fix this, we should change 'nam' to 'name'. Then re-run it.

# TypeError practice
a = 10
b = 5
print("a:", type(a), "b:", type(b))
print(a + b)

# This is a TypeError. It occurs on line 22 in the file bug3.py. Right before it crashes, the code is applying a plus operator between 'a' and 'b'. I'll inspect state by printing out the types 
# of each variable. We can see that 'a' is an integer and 'b' is a string. The 'plus' operator has a different underlying operation for each type, and they are not comptatible with each other, 
# so the program crashes. To fix this, we should convert both variables to the same type so they have the same legal operations. as the variable values here are integers, we can convert b to 
# an integer. Then re-run it.

# KeyError practice
user = {"name": "Jaclyn", "age": 23}
#print(user["email"])

# SOLUTION 1
print(user["age"])

# SOLUTION 2
if ("email" in user):
    print(user["email"])
else:
    print("key 'email' not found in user dictionary.")

user["email"] = "johnsmith@coding.ca"
print(user["email"])

# This is a KeyError. It occurs on line 30 in the file bug3.py. Right before it crashes, we see that the code is trying to print the value associated with the key "email" in the 
# dictionary assigned to 'user'. I'll inspect state by confirming if the dict has the key using the in function. As such, there is no key for "email" in the dictionary. 
# To fix this, depending on problem context, we could either add an "email" key value pair to the dictionary, or we could change the key access to a key that does exist, such as 
# "name" or "age". Then re-run it.

# AttributeError practice
x = 123
print(x.lower())
# This is an AttributeError. It occurs on line 52 in the file bug3.py. Right before it crashes, we see that the code is trying to perform a 'lower' operation on the integer variable 'x'.
# However, the 'lower' operation is only defined for string types, where it converts all uppercase letters to lowercase letters. To fix this, we should consider problem context. If 123 is 
# meant to be a string, we can convert it to a string. If 123 is meant to be an integer, we should remove the 'lower' operation and use a defined integer operation instead. Then re-run it.