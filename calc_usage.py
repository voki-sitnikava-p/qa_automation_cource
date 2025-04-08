from calculator import BasicCalc, NewСalc, initialization_cache, timer

with timer():
    for i in initialization_cache(200):  # Выполняем инициализацию изначальных значений для кэша факториалов
        pass

with timer():  #Выполняем рассчет факториала
   number = 200
   result = BasicCalc.factorial(number)
print(result)

# if __name__ == '__main__':
#     with timer():
#        result = NewСalc.calculate_user_input()
#        print(result)
