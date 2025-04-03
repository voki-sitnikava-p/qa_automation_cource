import re
import pickle

class BasicCalc:
    log = dict()

    @staticmethod
    def argument_checking(first_number, second_number):
        if not isinstance(first_number, (int, float)):
            BasicCalc.log['first_number_Type_Error'] = 'Invalid format of first number. Number replaced with 0'
            first_number = 0
        if not isinstance(second_number, (int, float)):
            BasicCalc.log['second_number_Type_Error'] = 'Invalid format of second number. Number replaced with 0'
            second_number = 0
        return first_number, second_number

    @staticmethod
    def sum_number(first_number, operation, second_number=None):
        if isinstance(first_number, (list, tuple, set)):
            result = 0
            for i in first_number:
                result += i
            BasicCalc.log_information(first_number, operation, second_number, result)
            return result
        else:
            first_number, second_number = BasicCalc.argument_checking(first_number, second_number)
            result = first_number + second_number
            BasicCalc.log_information(first_number, operation, second_number, result)
            return result

    @staticmethod
    def subtraction_number(first_number, operation, second_number):
        first_number, second_number = BasicCalc.argument_checking(first_number, second_number)
        result = first_number - second_number
        BasicCalc.log_information(first_number, operation, second_number, result)
        return result

    @staticmethod
    def division_number(first_number, operation, second_number):
        first_number, second_number = BasicCalc.argument_checking(first_number, second_number)
        try:
            result = first_number / second_number
        except ZeroDivisionError:
            BasicCalc.log['operation_error'] = 'ZeroDivisionError'
            print('You can"t divide by 0')
            result = None
            BasicCalc.log_information(first_number, operation, second_number, result)
        else:
            BasicCalc.log_information(first_number,operation, second_number, result)
            return result

    @staticmethod
    def multiplication_number(first_number, operation, second_number):
        first_number, second_number = BasicCalc.argument_checking(first_number, second_number)
        result = first_number * second_number
        BasicCalc.log_information(first_number, operation, second_number, result)
        return result

    operation_list = {'+': sum_number.__func__,
                      '-': subtraction_number.__func__,
                      '*': multiplication_number.__func__,
                      '/': division_number.__func__
                      }

    @staticmethod
    def enter_math_expression():
        math_expression = input('Enter a mathematical expression:')
        pattern = r'(?:\d+(?:\.\d*)?|\.\d+)[-+/*](?:\d+(?:\.\d*)?|\.\d+)'
        while re.fullmatch(pattern, math_expression) == None:
            math_expression = input('The mathematical expression entered is incorrect.\nPlease re-enter it:')
        return math_expression

    @staticmethod
    def arguments_operation(math_expression):
        try:
            arguments = re.match(r'((?:\d+(?:\.\d*)?|\.\d+))([-+/*])((?:\d+(?:\.\d*)?|\.\d+))', math_expression)
            first_number = arguments.group(1)
            second_number = arguments.group(3)
            operation = arguments.group(2)
        except AttributeError:
            print('The mathematical expression entered is incorrect')
            return None, None, None
        except TypeError:
            print('The mathematical expression entered is incorrect')
            return None, None, None
        else:
            return float(first_number), operation, float(second_number)

    @staticmethod
    def calculate_user_input():
        math_expression = BasicCalc.enter_math_expression()
        first_number, operation, second_number = BasicCalc.arguments_operation(math_expression)
        result = BasicCalc.operation_list[operation](first_number, operation, second_number)
        return result

    @staticmethod
    def log_information(first_number, operation, second_number, result):
        BasicCalc.log.update({"first_argument": first_number, "second_argument": second_number, "operation": operation, "result": result})
        with open('log.txt', 'w') as file:
            file.write(str(BasicCalc.log))
        # with open('log.txt', 'wb') as file:
        #     pickle.dump(BasicCalc.log, file)


class New_calc(BasicCalc):

    @staticmethod
    def memory():
        try:
            with open('memory.txt', 'r') as file:
                return file.read().split()
        except FileNotFoundError:
            BasicCalc.log['memory_error'] = 'FileNotFoundError'
            return list()

    @staticmethod
    def memo_minus(stack):
        stack = New_calc.memory()
        return stack.pop()

    @staticmethod
    def memo_plus(result):
        stack = New_calc.memory()
        if isinstance(result, (int, float)):
            if len(stack) == 3:
                New_calc.memo_minus(stack)
                stack.append(result)
            else:
                stack.append(result)
            str_stack = [str(num) for num in stack]
            with open('memory.txt', 'w') as file:
                file.write(' '.join(str_stack))
        else:
            print('The result cannot be written to file. Result must be a number.')

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
            math_expression = input('Number or operation entered is incorrect.\nPlease re-enter it: ')
        return math_expression

    @staticmethod
    def arguments_operation(math_expression):
        try:
            arguments = re.match(r'((?:\d+(?:\.\d*)?|\.\d+))([-+/*])', math_expression)
            first_number = arguments.group(1)
            second_number = New_calc.number_from_member()
            operation = arguments.group(2)
        except AttributeError:
            print('Number or operation entered is incorrect')
            return None, None, None
        except TypeError:
            print('The mathematical expression entered is incorrect')
            return None, None, None
        else:
            return float(first_number), operation, float(second_number)

    @staticmethod
    def calculate_user_input():
        math_expression = New_calc.enter_math_expression()
        first_number, operation, second_number = New_calc.arguments_operation(math_expression)
        result = BasicCalc.operation_list[operation](first_number, operation, second_number)
        New_calc.memo_plus(result)
        return result


#Ниже проверки работы калькулятора

if __name__ == '__main__':
   # result = New_calc.calculate_user_input()
   # print(result)
   first_number = 'ggf'
   second_number = '88'
   operation = '+'
   res = BasicCalc.division_number(first_number, operation, second_number)
   print(res)




