# Задача 22:
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа,
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества.
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

# import random

# n = int(input("Введите количесво элементов 1-го множества: "))
# m = int(input("Введите количесво элементов 2-го множества: "))
# print()

# # list_1 = [random.randint(0, 9) for i in range(n)]
# # list_2 = [random.randint(0, 9) for i in range(m)]

# list_1 = [int(input(f"Введите {i+1} элемент 1-го множества: ")) for i in range(n)]
# print()
# list_2 = [int(input(f"Введите {i+1} элемент 2-го множества: ")) for i in range(n)]
# print()

# print("Множество 1: ", list_1)
# print("Множество 2: ", list_2)
# print()

# result_list = []
# for i in list_1:
#     if i in list_2 and not i in result_list:
#         result_list.append(i)

# print("Повторяющиеся числа в порядке возрастания: ", sorted(result_list))


# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке,
# причём кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних.
# Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод
# — на i-ом кусте выросло ai ягод.

# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за
# один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.


# import random

# n = int(input("Количество кустов ня грядке: : "))
# garden_bed = [random.randint(0, 9) for i in range(n)]

# print(garden_bed)

# result_berries_sum = 0

# for i in range(n):
#     current_sum = garden_bed[i-1] + garden_bed[i] + garden_bed[(i+1)%n]
#     if current_sum > result_berries_sum:
#         result_berries_sum = current_sum

# print(result_berries_sum)