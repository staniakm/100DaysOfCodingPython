def add(a, b):
    return a + b


def substract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


possible_operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}


def calculator(a, b, operation):
    function = possible_operations[operation]
    return function(a, b)


number_a = int(input("Give me first number"))
for operation in possible_operations:
    print(operation)

operation = input("What operation?")

number_b = int(input("Give me second number"))

print(calculator(a=number_a, b=number_b, operation=operation))
