# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1

# result = 0
# number_N = int(input("Введдите количество элементов массива: "))
# array_A = []

# for i in range(number_N):
#     array_A.append(i + 1)

# print(array_A)
# number_X = int(input("Введите искомое число: "))

# result = 0
# list_1 = [1, 2, 3,3, 3, 4, 5]
# k = 3
# print(len(list_1))
# for i in range(len(list_1)):
#     if k == list_1[i]:
#         result+=1
# print(result)


# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5


# list_1 = [1, 2, 3, 4, 5]
# k = 6

# diff = 0
# result = k
# # print(len(list_1))
# for i in range(len(list_1)):
#     diff = k - list_1[i]
#     if diff < result:
#         result = diff
#         # print(result)
#         # print(diff)
# print(result)

# list_1 = [1, 12, 6, 7, 8, 15]
# k = 11


# diff = 0
# result = k
# max = 0
# # print(len(list_1))
# for i in range(len(list_1)):
#     diff = k - list_1[i]
#     if diff < result:
#         result = diff
#         max = list_1[i]
#         print(result)
#         print(diff)
#         print(max)
# print(max)

# Решение

# # list_1 = [1, 2, 3, 4, 5]
# # k = 6


# # list_1 = [2, 4, 1, 6, 8, 2, 9, 3, 2, 5]
# # k = 10
# min = k
# min_dif = 0
# for i in list_1:
#     if abs(i-k)<min:
#         min_dif = i
#         min = abs(i-k)
# print(min_dif)


# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.
# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только
# английские, либо только русские буквы.


# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только
# английские, либо только русские буквы.

# rus = {
#     1: ["А", "В", "Е", "И", "Н", "О", "Р", "С", "Т"],
#     2: ["Д", "К", "Л", "М", "П", "У"],
#     3: ["Б", "Г", "Ё", "Ь", "Я"],
#     4: ["Й", "Ы"],
#     5: ["Ж", "З", "Х", "Ц", "Ч"],
#     8: ["Ш", "Э", "Ю"],
#     10: ["Ф", "Щ", "Ъ"],
# }
# eng = {
#     1: ["A", "E", "I", "O", "U", "L", "N", "S", "T", "R"],
#     2: ["D", "G"],
#     3: ["B", "C", "M", "P"],
#     4: ["F", "H", "V", "W", "Y"],
#     5: ["K"],
#     8: ["J", "X"],
#     10: ["Q", "Z"],
# }

# # k = input().upper()


# import re


# def сyrillic(k):
#     return bool(re.search("[а-яА-Я]", k))


# if сyrillic(k):
#     print(sum([k for i in k for k, v in rus.items() if i in v]))
# else:
#     print(sum([k for i in k for k, v in eng.items() if i in v]))


k = "НОУТБУК"

# Введите ваше решение ниже

dictionary = {
    1: ["А", "В", "Е", "И", "Н", "О", "Р", "С", "Т"],
    2: ["Д", "К", "Л", "М", "П", "У"],
    3: ["Б", "Г", "Ё", "Ь", "Я"],
    4: ["Й", "Ы"],
    5: ["Ж", "З", "Х", "Ц", "Ч"],
    8: ["Ш", "Э", "Ю"],
    10: ["Ф", "Щ", "Ъ"],
    1: ["A", "E", "I", "O", "U", "L", "N", "S", "T", "R"],
    2: ["D", "G"],
    3: ["B", "C", "M", "P"],
    4: ["F", "H", "V", "W", "Y"],
    5: ["K"],
    8: ["J", "X"],
    10: ["Q", "Z"],
}
word = k.upper()

point_sum = 0

for i in word:
    for x, y in dictionary.items():
        if i in y:
            point_sum += x
print(point_sum)