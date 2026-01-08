# Define arithmetic functions
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Error! Division by zero."
# Main program
print("Select Operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter choice (1/2/3/4): ")
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
try:
    if choice == '1':
        print(f"Result: {add(x, y)}")
    elif choice == '2':
        print(f"Result: {subtract(x, y)}")
    elif choice == '3':
        print(f"Result: {multiply(x, y)}")
    elif choice == '4':
        print(f"Result: {divide(x, y)}")
    else:
        print("Invalid Input!")
except ValueError:
    print("Error! Please enter valid numbers.")