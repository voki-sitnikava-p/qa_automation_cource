import re
def sum_number(first_number = None, second_number = None):
    if first_number == None:
        print(f'The result of the sum {first_number} = {sum([i for i in second_number])}')
    elif second_number == None:
        print(f'The result of the sum {first_number} = {sum([i for i in first_number])}')
    else:
        print(f'The result of the expression {math_expression} = {first_number + second_number}')

def subtraction_number(first_number, second_number):
    print(f'The result of the expression {math_expression} = {first_number - second_number}')

def division_number(first_number, second_number):
    print(f'The result of the expression {math_expression} = {first_number / second_number}')

def multiplication_number(first_number, second_number):
    print(f'The result of the expression {math_expression} = {first_number * second_number}')

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

math_expression = enter_math_expression()

operation = [i for i in math_expression if i in '-+/*'][0]
numbers = math_expression.split(operation)
first_number = float(numbers[0])
second_number = float(numbers[1])

operation_list[operation](first_number, second_number)