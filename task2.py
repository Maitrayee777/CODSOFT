# Task 2
def add(a, b):
    return a + b

def subtract(c, d):
    return c - d

def multiply(x, y):
    return x * y

def divide(y, z):
    if z != 0:
        return y / z
    else:
        return "Cannot divide by zero"

print("Simple Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# Getting inputs from user
number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))
operation = input("Enter operation of your choice(1/2/3/4): ")

# Performing required calculations 
if operation == '1':
    result = add(number1, number2)
    print(f"{number1} + {number2} = {result}")
elif operation == '2':
    result = subtract(number1, number2)
    print(f"{number1} - {number2} = {result}")
elif operation == '3':
    result = multiply(number1, number2)
    print(f"{number1} * {number2} = {result}")
elif operation == '4':
    result = divide(number1, number2)
    print(f"{number1} / {number2} = {result}")
else:
    print("Invalid operation. Please enter a valid operation from (1/2/3/4).")
