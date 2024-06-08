import re

def parse_input(input_str):
    match = re.match(r"(\d+)([+\-*/])(\d+)", input_str)
    if not match:
        raise ValueError("Invalid input format")
    return float(match.group(1)), match.group(2), float(match.group(3))

def calculate(parsed_input):
    num1, operation, num2 = parsed_input

    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2
    else:
        raise ValueError("Invalid operation")

if __name__ == "__main__":
    input_str = input("Enter your first number, operation, and second number (e.g., 3+4): ")
    try:
        parsed_input = parse_input(input_str)
        result = calculate(parsed_input)
        print(f"The result is: {result}")
    except ValueError as e:
        print(e)
