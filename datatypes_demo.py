# Task 2: Variables, Data Types & Type Conversion
# Python Developer Internship

# Integer variable
age = 20

# Float variable
height = 5.6

# String variable
name = "Sanjana"

# Boolean variable
is_student = True

# Printing values
print("Age:", age)
print("Height:", height)
print("Name:", name)
print("Is Student:", is_student)

print("\n--- Data Types ---")
print(type(age))
print(type(height))
print(type(name))
print(type(is_student))

# Arithmetic operations
a = 10
b = 3

print("\n--- Arithmetic Operations ---")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

# Type conversion: String to Integer
print("\n--- Type Conversion ---")
try:
    num = input("Enter a number: ")
    num = int(num)  # converting string to integer
    print("Number + 5 =", num + 5)
except:
    print("Invalid input! Please enter a valid integer.")

# String and number concatenation
marks = 85
print("\n--- String Concatenation ---")
print("My marks are " + str(marks))

# Dynamic typing demonstration
print("\n--- Dynamic Typing ---")
x = 100
print(x, type(x))

x = "Python Programming"
print(x, type(x))