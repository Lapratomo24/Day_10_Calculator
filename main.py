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


num1 = int(input("What is your first number? "))
num2 = int(input("What is your second number? "))
for op in operations:
    print(op, end=" ")
selection = input(" <-- Pick a mathematical operation: ")

math_operation = operations[selection]
result = math_operation(num1, num2)
print(f"{num1} {selection} {num2} = {result}")
    
end_calculation = False
    
while not end_calculation:
    new_calc = input(f"Type 'y' to continue calculating with {result}, or 'n' to stop: ")
    if new_calc == 'n':
        end_calculation = True
    else:
        next_op = input("Pick a mathematical operation: ")
        num3 = int(input("What is your next number? "))

        math_operation = operations[next_op]
        result = math_operation(result, num3)
        print(f"{result} {next_op} {num3} = {result}")
