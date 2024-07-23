# Calculator

from logo import logo
print(logo)

# addition
def add(a, b):
    return a + b

# subtraction
def subtract(a, b):
    return a - b

#multiply
def multiply(a, b):
    return a * b

#division
def divide(a, b):
    return a / b

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    num1 = float(input("What is your first number? "))

    for op in operations:
        print(op, end=" ")
        
    end_calculation = False

    while not end_calculation:
        selection = input(" <-- Pick a mathematical operation: ")
        num2 = float(input("What is your other number? "))

        math_operation = operations[selection]
        result = math_operation(num1, num2)
        print(f"{num1} {selection} {num2} = {result}")
        
        new_calc = input(f"Type 'y' to continue calculating with {result}, or 'n' to start a new calculation: ")
        if new_calc == 'n':
            end_calculation = True
        elif new_calc == 'y':
            num1 = result
            calculator()

calculator()