# Variables + Types
print("Variables + Types Section\n")
age = 21
height = 155.5
name = "Jaclyn"
is_student = True

print("age:", age, "|", "type:", type(age))
print("height:", height, "|", "type:", type(height)) 
print("name:", name, "|", "type:", type(name)) 
print("is_student:", is_student, "|", "type:", type(is_student))

age = age + 1
print("age:", age)

# I/O + Formatting

print("\nI/O + Formatting Section\n")
# name = input("What is your name? ")
#age = input("How old are you? ")

name = "jjbeans"
age = 22

# print("Hello, " + name + "! You are " + age + " years old.")
print(f"Hello, {name}! You are {age} years old.")

age = int(age) + 1
print(type(age))

# Operators + Expressions
print("\nOperators + Expressions Section\n")
x = 10
y = 3

print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
print("Floor Division:", x // y)
print("Modulus:", x % y)
print(f"Exponentiation of {x} to the power of {y}:", x ** y)

# Comparisons + Logical Operators

print("Is x greater than y?", x > y)
print("Is x equal to y?", x == y)
print("Is x not equal to y?", x != y)
print("Logical AND:", (x > 5) and (y < 5))
print("Logical OR:", (x > 5) or (y > 5))
print("Logical NOT:", not(x > 5))
print("Combined Expression:", (x + y) * (x - y))

# Conditionals
print("\nConditionals Section\n")
if age < 18:
    print("You are a minor.")
elif age >= 65:
    print("You are a senior citizen.")
else:
    print("You are an adult.")

# Loops
print("\nLoops Section\n")
for i in range(5):
    print(i)

count = 0

while count < 5:
    print(count)
    count = count + 1

# Loop patterns

print("\nLoop Patterns Section\n")

# Counter
# counts iterations
print("Counter Pattern:")
count = 0
while count < 10:
    count += 1

# Accumulator
# combines values over time
print("Accumulator Pattern:")
total = 0

for i in range(1, 6):
    total += i

print(total)

# Event-controlled loop
print("Event-Controlled Loop Pattern:")
number = 0
while number != 5:
    number = int(input("Enter a number (5 to stop): "))
print("Exited event-controlled loop.")

# Fixed-count loop
print("Fixed-Count Loop Pattern:")

for i in range(3):
    print(f"Iteration {i + 1}")

# Fixed-count loop using while
count = 0
while count < 3:
    print(f"Iteration {count + 1}")
    count += 1

# Sentinel loop
while True:
    command= input("Enter 'exit' to quit: ")
    if command == 'exit':
        break
print("Exited sentinel loop.")

# Nested loops
print("\nNested Loops Section\n")
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")    