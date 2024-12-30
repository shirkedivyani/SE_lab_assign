def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Returns the difference of two numbers."""
    return a - b

def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b

def divide(a, b):
    """Returns the division of two numbers. Raises an error if dividing by zero."""
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b



if __name__ == "__main__":
    print("Simple Calculator")
    print("Options: add, subtract, multiply, divide")
    operation = input("Enter the operation: ").strip().lower()
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))

    try:
        if operation == "add":
            print("Result:", add(a, b))
        elif operation == "subtract":
            print("Result:", subtract(a, b))
        elif operation == "multiply":
            print("Result:", multiply(a, b))
        elif operation == "divide":
            print("Result:", divide(a, b))
        else:
            print("Invalid operation")
    except ValueError as e:
        print("Error:", e)
