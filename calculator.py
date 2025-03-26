from mymodule import BasicCalc
from mymodule import New_calc
from mymodule import initialization_cache

# if __name__ == '__main__':
#    result = BasicCalc.calculate_user_input()
#    print(result)
   # first_number = [33, 4, 66]
   # operation = '+'
   # first_number = BasicCalc.sum_number(first_number, operation)
   # print(first_number)

# if __name__ == '__main__':
#     with BasicCalc.timer():
#        result = New_calc.calculate_user_input()
#        print(result)


with BasicCalc.timer():
    for i in initialization_cache(200):  # Выполняем инициализацию изначальных значений для кэша факториалов
        pass

with BasicCalc.timer():  #Выполняем рассчет факториала
   number = 200
   result = BasicCalc.factorial(number)
print(result)