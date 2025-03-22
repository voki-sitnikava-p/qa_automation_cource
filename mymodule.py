import re
import os

class BasicCalc:

    @staticmethod
    def sum_number(first_number, second_number=None):
        if hasattr(first_number, '__iter__'):
            iter_sum = 0
            for i in first_number:
                iter_sum += i
            return iter_sum
        else:
            return first_number + second_number

    @staticmethod
    def subtraction_number(first_number, second_number):
        return first_number - second_number

    @staticmethod
    def division_number(first_number, second_number):
        return first_number / second_number

    @staticmethod
    def multiplication_number(first_number, second_number):
        return first_number * second_number

    @staticmethod
    def enter_math_expression():
        math_expression = input('Enter a mathematical expression:')
        pattern = r'(?:\d+(?:\.\d*)?|\.\d+)[-+/*](?:\d+(?:\.\d*)?|\.\d+)'
        while re.fullmatch(pattern, math_expression) == None:
            math_expression = input('The mathematical expression entered is incorrect.\nPlease re-enter it:')
        return math_expression

    @staticmethod
    def arguments_operation(math_expression):
        arguments = re.match(r'((?:\d+(?:\.\d*)?|\.\d+))([-+/*])((?:\d+(?:\.\d*)?|\.\d+))', math_expression)
        first_number = arguments.group(1)
        second_number = arguments.group(3)
        operation = arguments.group(2)
        return float(first_number), float(second_number), operation

    @staticmethod
    def calculate_user_input():
        math_expression = BasicCalc.enter_math_expression()
        first_number, second_number, operation = BasicCalc.arguments_operation(math_expression)
        result = BasicCalc.operation_list[operation](first_number, second_number)
        return result


BasicCalc.operation_list = {'+': BasicCalc.sum_number,
                      '-': BasicCalc.subtraction_number,
                      '*': BasicCalc.multiplication_number,
                      '/': BasicCalc.division_number
                      }


class New_calc(BasicCalc):

    @staticmethod
    def memory():
        if os.path.exists('memory.txt'):
            with open('memory.txt', 'r') as file:
                return file.read().split()
        else:
            return list()

    @staticmethod
    def memo_minus(stack):
        return stack.pop()

    @staticmethod
    def memo_plus(result):
        stack = New_calc.memory()
        if len(stack) == 3:
            New_calc.memo_minus(stack)
            stack.append(result)
        else:
            stack.append(result)
        str_stack = [str(num) for num in stack]
        with open('memory.txt', 'w') as file:
            file.write(' '.join(str_stack))

    @staticmethod
    def number_from_member():
        if len(New_calc.memory()) == 0:
            return 0
        else:
            return New_calc.memory()[-1]

    @staticmethod
    def enter_math_expression():
        math_expression = input('Enter number and operation: ')
        pattern = r'(?:\d+(?:\.\d*)?|\.\d+)[-+/*]'
        while re.fullmatch(pattern, math_expression) == None:
            math_expression = input('Number and operation entered is incorrect.\nPlease re-enter it: ')
        return math_expression

    @staticmethod
    def arguments_operation(math_expression):
        arguments = re.match(r'((?:\d+(?:\.\d*)?|\.\d+))([-+/*])', math_expression)
        first_number = arguments.group(1)
        second_number = New_calc.number_from_member()
        operation = arguments.group(2)
        return float(first_number), float(second_number), operation

    @staticmethod
    def calculate_user_input():
        math_expression = New_calc.enter_math_expression()
        first_number, second_number, operation = New_calc.arguments_operation(math_expression)
        result = BasicCalc.operation_list[operation](first_number, second_number)
        New_calc.memo_plus(result)
        return result
