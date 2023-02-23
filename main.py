import numpy as np # Все функции были взяты с https://numpy.org/doc/stable/index.html , мне удобнее работать с оригинальной документацией , находя функцию , которая мне нужна по поиску в документации
import colorama
from colorama import Fore


# 1 пункт , среднее арифметическое входного массива .mean()
print(Fore.YELLOW + "1 пункт задания")
# Создаём сам массив
arr = np.array([1,2,3,4,5,6,7,8,9,10])
# Используем дефолтную функцию библиотеки нумпай
mean = np.mean(arr)
print(Fore.MAGENTA +"Среднее арифметическое массива: ", mean, "\n")

# 2 пункт , всё то же самое , но найти максимальное значение , будем использовать тот же массив что и из пункта 1
print(Fore.YELLOW +"2 пункт задания")
# Создадим переменную amax и поместим в неё максимальное значение массива с помощью функции нампая
maxa = np.amax(arr)
print(Fore.MAGENTA +"Максимальное значение массива:", maxa, "\n")

#3 пункт , инверсия второго , тоесть минимальное значение
print(Fore.YELLOW +"3 пункт задания")
# Также создаём переменную
minx = np.amin(arr)
print(Fore.MAGENTA +"Минимальное значение массива:",minx, "\n")

#4 пункт , ничего сложного , используем все те же встроенные функции либы
print(Fore.YELLOW +"4 пункт задания")
argmaxa = np.argmax(arr)
print(Fore.MAGENTA +"Индекс максимального элемента массива:", argmaxa, "\n")

#5 пункт , инверсия 4
print(Fore.YELLOW +"5 пункт задания")
argmina = np.argmin(arr)
print(Fore.MAGENTA +"Индекс минимального элемента массива:", argmina, "\n")

#6 пункт , задача немного поменялась и нам нужен массив с отрицательными числами
print(Fore.YELLOW +"6 пункт задания")
arr1 = np.array([1,-2,3,-4,5,-6,7,-8,9,-10])
# https://numpy.org/doc/stable/reference/generated/numpy.maximum.html , голова взрывается от количества возможных параметров у этой функции , лучше матлаба
otric = np.maximum(arr1, 0)
print(Fore.MAGENTA +"Заменённый массив , где число <0 превращается в 0:", "\n", otric)

#7 пункт инверсия 6
print(Fore.YELLOW +"7 пункт задания:")
poloz = np.minimum(arr1, 0)
print(Fore.MAGENTA +"Заменённый массив , где число >0 превращается в 0:", "\n", poloz)

#8 пункт
print(Fore.YELLOW +"8 пункт")
st3 = np.power(arr, 3)
print(Fore.MAGENTA +"Первый массив ,возведённый в 3 степень:","\n", st3, "\n")

#9 пункт
print(Fore.YELLOW +"9 пункт")
sq = np.sqrt(arr)
print(Fore.MAGENTA +"Квадратный корень каждого элемента массива:", "\n", sq, "\n")

# 10 пункт
print(Fore.YELLOW +"10 пункт")
sm = np.sum(arr1)
print(Fore.MAGENTA + "Сумма элементов массива:", sm)




