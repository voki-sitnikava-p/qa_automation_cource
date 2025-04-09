from calculator import BasicCalc, NewCalc, initialization_cache, timer

if __name__ == '__main__':
    calc1 = BasicCalc()
    calc2 = NewCalc()
    calc1.count_random_numbers()  # Проверка распределения для генерации случайных целых чисел
    result = calc1.calculate_user_input()  # Выполнение NewCalc, проверка записи даты в лог
    print(result)
    with timer():
        for i in initialization_cache(200):  # Выполняем инициализацию изначальных значений для кэша факториалов
            pass
    with timer():  # Выполняем рассчет факториала
        result = calc1.factorial(600)
        print(result)
    with timer():  # Выполняем рассчет факториала с помощью math.factorial()
        result = calc1.factorial_from_math(600)
        print(result)
