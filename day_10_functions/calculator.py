possible_operations = ["+", "-", "*", "/"]


def add(a, b):
    return a + b


def substract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def calculator(a, b, operation):
    if operation == "+":
        return add(a, b)
    elif operation == "-":
        return substract(a, b)
    elif operation == "*":
        return a * b
    elif operation == "/":
        return divide(a, b)
    else:
        print("Invalid operation")


number_a = int(input("Give me first number"))
for operation in possible_operations:
    print(operation)

operation = input("What operation?")

number_b = int(input("Give me second number"))

print(calculator(a=number_a, b=number_b, operation=operation))
