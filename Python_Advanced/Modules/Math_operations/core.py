class InvalidOperator(Exception):
    pass

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b
def power(a, b):
    return a ** b

def do_math_operations(math_expr):
    math_expr_list = math_expr.split()
    number1 = float(math_expr_list[0])
    number2 = int(math_expr_list[2])
    operator = math_expr_list[1]
    if operator == '+':
        return add(number1, number2)
    elif operator == '-':
        return subtract(number1, number2)
    elif operator == '*':
        return multiply(number1, number2)
    elif operator == '/':
        return divide(number1, number2)
    elif operator == '^':
        return power(number1, number2)
    else:
        raise InvalidOperator(f"Invalid operator {operator} for math operations")