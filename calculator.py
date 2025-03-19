import re

def sum_number(first_number, second_number = None):
    if hasattr(first_number, '__iter__'):
        return sum([i for i in first_number])
    else:
        return first_number + second_number

def subtraction_number(first_number, second_number):
    return first_number - second_number

def division_number(first_number, second_number):
    return first_number / second_number

def multiplication_number(first_number, second_number):
    return first_number * second_number

operation_list = {'+': sum_number,
                  '-': subtraction_number,
                  '*': multiplication_number,
                  '/': division_number
}

def enter_math_expression():
    math_expression = input('Enter a mathematical expression:')
    pattern = r'(?:\d+(?:\.\d*)?|\.\d+)[-+/*](?:\d+(?:\.\d*)?|\.\d+)'
    while re.fullmatch(pattern, math_expression) == None:
        math_expression = input('The mathematical expression entered is incorrect.\nPlease re-enter it:')
    return math_expression

def arguments_operation(math_expression):
    arguments = re.match(r'((?:\d+(?:\.\d*)?|\.\d+))([-+/*])((?:\d+(?:\.\d*)?|\.\d+))', math_expression)
    first_number = arguments.group(1)
    second_number = arguments.group(3)
    operation = arguments.group(2)
    return float(first_number), float(second_number), operation

if __name__ == '__main__':
    math_expression = enter_math_expression()
    first_number, second_number, operation = arguments_operation(math_expression)
    result = operation_list[operation](first_number, second_number)
