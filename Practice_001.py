def operation():
    print('''Type the symbol of operation you want to use
    (+) Addition
    (-) Subtraction
    (*) Multiplication
    (/) Division
    
Press "Enter" when done.''')


def process(operation, first_value, second_value):
    value_outcome = 0
    if operation == '+':
        value_outcome = (first_value + second_value)
    elif operation == '-':
        value_outcome = (first_value - second_value)
    elif operation == '*':
        value_outcome = (first_value * second_value)
    elif operation == '/':
        value_outcome = (first_value / second_value)
    else:
        print("Error: Invalid input. Please try again.")
        exit()

    result = format(value_outcome, ",.2f")

    return result

first_value = 0
second_value = 0

print("Simple Calculator by Python")
first_input = input("Enter the first value: ")

if not first_input.replace(".", "").replace("-", "").isnumeric():
    print("Error: Invalid input. Please enter numerical values and try again.")
    exit()
else:
    first_value = float(first_input)

second_input = input("Enter the second value: ")

if not second_input.replace(".", "").replace("-", "").isnumeric():
    print("Error: Invalid input. Please enter numerical values and try again.")
    exit()
else:
    second_value = float(second_input)

operation()
chosen_operation = input("\nType here: ")
result = process(chosen_operation, first_value, second_value)

print(f"\nSolution: {format(first_value, ',.2f')} {chosen_operation} {format(second_value, ',.2f')}")
print(f"Result: {result}")

# Programmed by Rowell Castro.
