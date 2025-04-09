from calculator import BasicCalc, NewСalc, initialization_cache, timer

if __name__ == '__main__':
    BasicCalc.count_random_numbers() #Проверка распределения для генерации случайных целых чисел
    result = NewСalc.calculate_user_input() #Выполнение NewCalc, проверка записи даты в лог
    # with BasicCalc.timer():
    #    for i in initialization_cache(200):  # Выполняем инициализацию изначальных значений для кэша факториалов
    #        pass
    with timer():  # Выполняем рассчет факториала
       number = 600
       result = BasicCalc.factorial(number)
       print(result)
    with timer():  # Выполняем рассчет факториала с помощью math.factorial()
       number = 600
       result = BasicCalc.factorial_from_math(number)
       print(result)

# if __name__ == '__main__':
#     with timer():
#        result = NewСalc.calculate_user_input()
#        print(result)
