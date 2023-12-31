# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.


num_1 = int(input("Введите первый элемент арифметической прогрессии: "))
difference = int(input("Разность элементов арифметической прогрессии: "))
amount = int(input("Введите количество элементов арифметической прогрессии: "))
print()

result_list=[]

for i in range(amount):
    an = num_1 + i * difference
    result_list.append(an)

print("Массив заполненный элементами арифметической прогрессии: ", result_list)

# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат
# заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

n =  int(input("Введите количество элементов списка: "))
list_1 = [random.randint(0, 100) for i in range(n)]
print()
print("Список случайных чисел от 0 до 99: ")
print(list_1)
print()

min_range = int(input("Введите минимальное значение диапазона: "))
max_range = int(input("Введите максимальное значение диапазона: "))
print()

result_list = []

for i in range(n):
    if list_1[i]>=min_range and list_1[i]<=max_range:
        result_list.append(i)

print(F"Индексы элементов списка, значения которых принадлежат диапазону от {min_range} до {max_range}: ")
print(result_list)