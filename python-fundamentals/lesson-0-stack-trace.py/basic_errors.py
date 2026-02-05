# Practicing with common Python runtime errors
# Goal: Goal: Practice stack tracing and fixing errors in Python code

# IndexError practice
nums = [10, 20, 30]
print("len:", len(nums), "|", "nums:", nums)
#print(nums[3])
print(nums[2])

# This is an IndexError. It occurs on line 4 in the file basic_errors.py. Right before it crashes, we see that nums is trying to be accessed at index 3. I'll inspect state by printing out
# the length of the list. Here we can see that nums is a list with only 3 elements, so its index goes from 0 to 2. Therefore, to fix this, we should change the index we are trying to 
# access from 3 to 2. Then re-run it.

# NameError practice
name = "jaclyn"
#print(nam)
print(name)

# This is a NameError. It occurs on line 12 in the file basic_errors.py. Right before it crashes, we see that the code is trying to print the variable 'nam'. I'll inspect state by checking the variable
# assignment. However, in this code the variable 'nam' is not defined, and what is defined instead is 'name'. Thus, to fix this, we should change 'nam' to 'name'. Then re-run it.

# TypeError practice
a = 10
b = 5
print("a:", type(a), "b:", type(b))
print(a + b)

# This is a TypeError. It occurs on line 22 in the file basic_errors.py. Right before it crashes, the code is applying a plus operator between 'a' and 'b'. I'll inspect state by printing out the types 
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

# This is a KeyError. It occurs on line 30 in the file basic_errors.py. Right before it crashes, we see that the code is trying to print the value associated with the key "email" in the 
# dictionary assigned to 'user'. I'll inspect state by confirming if the dict has the key using the in function. As such, there is no key for "email" in the dictionary. 
# To fix this, depending on problem context, we could either add an "email" key value pair to the dictionary, or we could change the key access to a key that does exist, such as 
# "name" or "age". Then re-run it.

# AttributeError practice
x = '123'
print(x.lower())
# This is an AttributeError. It occurs on line 52 in the file basic_errors.py. Right before it crashes, we see that the code is trying to perform a 'lower' operation on the integer variable 'x'.
# However, the 'lower' operation is only defined for string types, where it converts all uppercase letters to lowercase letters. To fix this, we should consider problem context. If 123 is 
# meant to be a string, we can convert it to a string. If 123 is meant to be an integer, we should remove the 'lower' operation and use a defined integer operation instead. Then re-run it.

# UnboundLocalError practice
x = 10

# INITIAL CODE
# def f():
#     print(x)
#     x = x + 1

# SOLUTION 1
def f():
    x = 3
    print(x)
    x = x + 1

f()

# This is an UnboundLocalError. It occurs on lines 65 and 68 in the file basic_errors.py. Right before it crashes, we see that Python is trying to print out the value assigned to 
# variable 'x'. However, it is not able to print a value because Python cannot find an associated value to x. This is because the x variable in the function only has a scope within
# the function. It does not register the value assigned to the x variable defined outside the function. I'll inspect state by printing out the value of the variable x 
# within the function. Doing that still got an unboundLocalError, which implies that we need to assign a value to the local variable x before using it. I'll assign the integer 3 
# before the code runs print() to fix this. Then we re-run it.

# ValueError practice
s = "10a"
# n = int(s)
#print(n)

# SOLUTION
n = int(s, 16)
print(n)

# This is a ValueError. It occurs on line 85 in the file basic_errors.py. Right before it crashes, we see that the code is trying to perform an int() conversion function on the 
# value of variable 's'. The error says that the code is using an invalid literal for the int() function, so let's research the function. From documentation, we can see that 
# the int() function technically takes in two arguments- value, and a base. If there is no second argument, the default value for the base is 10. Now when we see the value of the
# string 's', we see that it contains the character A, which is a hexadecimal number of the base 16 system. Next step requires problem context. Do we want to split this into 10 
# as base 10 and A as a separate hexadecimal number? For now, let's assume that the entire string is one hexadecimal number. To fix this, we should explicitly include a second 
# argument overriding the default base value of 10, and replace it with base 16. Then re-run it.  

# ZeroDivisionError practice

total = 10
#count = 0
count = 1 # SOLUTION
average = total / count
print(average)

# This is a ZeroDivisionError. It occurs on line 103 in file basic_errors.py. Right before it crashes, we see that the code is trying to divide the value of 'total' by the value 
# of 'count'. I'll inspect state by printing out the value of count, and we see that it is zero. By mathematical principles, the code cannot divide by zero, so it crashes. 
# To fix this, we can assign a non-zero value to count. The exact value depends on problem context. Just for simplicity, let's assign the smallest integer value to count, which 
# is 1. Then re-run it.

