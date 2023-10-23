# defining functions for addition, subtraction, multiplication and division
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

# taking input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# displaying the menu
print("Menu:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# taking input from the user to select the operation
choice = input("Enter choice (1/2/3/4): ")

# performing the selected operation and displaying the result
if choice == '1':
    print(num1, "+", num2, "=", add(num1,num2))

elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1,num2))

elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1,num2))

elif choice == '4':
    print(num1, "/", num2, "=", divide(num1,num2))

else:
    print("Invalid input")
