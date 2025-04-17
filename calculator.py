import re
import pickle
import time
from contextlib import contextmanager
import sys
import datetime
from random import randint
from collections import Counter
from typing import Union

sys.setrecursionlimit(2000)


@contextmanager
def timer():
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print(f"Время выполнения: {end - start:.6f} секунд")


def initialization_cache(number):
    if number < 0:
        raise ValueError("Number must be positive")
    for i in range(number + 1):
        BasicCalc.factorial(i)
        yield
    print('Инициализация изначальных значений для кэша факториалов завершена')


def cache(func):
    try:
        with open('cache.pkl', 'rb') as file:
            cache = pickle.load(file)
    except FileNotFoundError:
        cache = dict()

    def wrapper(number):
        if number in cache:
            return cache[number]
        else:
            result = func(number)
            cache[number] = result
            with open('cache.pkl', 'wb') as file:
                pickle.dump(cache, file)
            return result

    return wrapper


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class BasicCalc(metaclass=SingletonMeta):
    log = dict()

    @staticmethod
    @cache
    def factorial(number):
        if number < 0:
            raise ValueError("Number must be positive")
        if number <= 1:
            return 1
        else:
            return number * BasicCalc.factorial(number - 1)

    def count_random_numbers(self):
        random_numbers = [randint(0, 50) for i in range(50)]
        distribution_numbers = Counter(random_numbers)
        print('Распределение для генерации случайных целых чисел:')
        for num in sorted(distribution_numbers):
            print(f'число {num}: {distribution_numbers[num]}')

    @staticmethod
    def argument_checking(first_number, second_number, operation):
        if not isinstance(first_number, (int, float)):
            BasicCalc.log['first_number_Type_Error'] = (
                'Invalid format of first number. Number replaced with 0'
            )
            first_number = 0
        if not isinstance(second_number, (int, float)):
            if operation == '/':
                BasicCalc.log['second_number_Type_Error'] = 'Invalid format of second number. Number replaced with 1'
                second_number = 1
            else:
                BasicCalc.log['second_number_Type_Error'] = 'Invalid format of second number. Number replaced with 0'
                second_number = 0
        return first_number, second_number

    @staticmethod
    def sum_number(first_number, operation, second_number=None):
        if isinstance(first_number, (list, tuple, set)):
            result = 0
            for i in first_number:
                result += i
            BasicCalc.log_information(
                first_number, operation, second_number, result
            )
            return result
        else:
            first_number, second_number = BasicCalc.argument_checking(first_number, second_number, operation)
            result = first_number + second_number
            BasicCalc.log_information(
                first_number, operation, second_number, result
            )
            return result

    @staticmethod
    def subtraction_number(first_number, operation, second_number):
        first_number, second_number = BasicCalc.argument_checking(first_number, second_number, operation)
        result = first_number + second_number
        BasicCalc.log_information(
            first_number, operation, second_number, result
        )
        return result

    @staticmethod
    def division_number(first_number, operation, second_number):
        first_number, second_number = BasicCalc.argument_checking(first_number, second_number, operation)
        try:
            result = first_number / second_number
        except ZeroDivisionError:
            BasicCalc.log['operation_error'] = 'ZeroDivisionError'
            print("You can't divide by 0")
            result = None
            BasicCalc.log_information(
                first_number, operation, second_number, result
            )
        else:
            BasicCalc.log_information(
                first_number, operation, second_number, result
            )
            return result

    @staticmethod
    def multiplication_number(first_number, operation, second_number):
        first_number, second_number = BasicCalc.argument_checking(first_number, second_number, operation)
        result = first_number * second_number
        BasicCalc.log_information(
            first_number, operation, second_number, result
        )
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
        while re.fullmatch(pattern, math_expression) is None:
            math_expression = input("The mathematical expression entered is incorrect.\n"
                                    "Please re-enter it:"
                                    )
        return math_expression

    @staticmethod
    def arguments_operation(math_expression):
        try:
            arguments = re.match(r"(\d+(?:\.\d*)?|\.\d+)([-+/*])(\d+(?:\.\d*)?|\.\d+)", math_expression)
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
        BasicCalc.log.update({"first_argument": first_number, "second_argument": second_number,
                              "operation": operation, "result": result,
                              "date_log": str(datetime.datetime.now())})
        with open('log.txt', 'w') as file:
            file.write(str(BasicCalc.log))
        # with open('log.txt', 'wb') as file:
        #     pickle.dump(BasicCalc.log, file)


class NewCalc(BasicCalc):

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
        return stack.pop()

    @staticmethod
    def memo_plus(result):
        stack = NewCalc.memory()
        if isinstance(result, (int, float)):
            if len(stack) == 3:
                NewCalc.memo_minus(stack)
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
        if len(NewCalc.memory()) == 0:
            return 0
        else:
            return NewCalc.memory()[-1]

    @staticmethod
    def enter_math_expression():
        math_expression = input('Enter number and operation: ')
        pattern = r'(?:\d+(?:\.\d*)?|\.\d+)[-+/*]'
        while re.fullmatch(pattern, math_expression) is None:
            math_expression = input('Number or operation entered is incorrect.\n'
                                    'Please re-enter it: '
                                    )
        return math_expression

    @staticmethod
    def arguments_operation(math_expression):
        try:
            arguments = re.match(r"(\d+(?:\.\d*)?|\.\d+)([-+/*])", math_expression)
            first_number = arguments.group(1)
            second_number = NewCalc.number_from_member()
            operation = arguments.group(2)
        except AttributeError:
            print("Number or operation entered is incorrect")
            return None, None, None
        except TypeError:
            print('The mathematical expression entered is incorrect')
            return None, None, None
        else:
            return float(first_number), operation, float(second_number)

    @staticmethod
    def calculate_user_input():
        math_expression = NewCalc.enter_math_expression()
        first_number, operation, second_number = NewCalc.arguments_operation(math_expression)
        result = BasicCalc.operation_list[operation](first_number, operation, second_number)
        NewCalc.memo_plus(result)
        return result
