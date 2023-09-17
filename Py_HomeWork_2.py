# Задача 10:
# На столе лежат n монеток. Некоторые из них лежат ввер решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки былjповернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

# 1. Решение через Count_________________
import random

# Вводим количество монеток
n = int(input("Введите количетсво монеток: "))
print()
minimalResult = 0

# Заполняем строку случайными символами из набора
coinSides = "OR"
randomString = " ".join(random.choice(coinSides) for i in range(n))

print("На столе лежит", n, "монеток в таком виде:", randomString)
print("Орлов: ", n - randomString.count("R"), "Решек: ", randomString.count("R"))

# Сравниваем количество орлов и решек
if n - randomString.count("R") < randomString.count("R"):
    minimalResult = n - randomString.count("R")
else:
    minimalResult = randomString.count("R")

print()
print("Минимальное количество монет, которые нужно перевернуть: ", minimalResult)
print()

# 2. Решение через for_________________

import random

n = int(input("Введите количетсво монеток: "))

minimalResult = 0

coinSides = [random.randint(0,1) for i in range(n)]
print("На столе лежит", n, "монеток в таком виде:", coinSides)

count = 0
for side in coinSides:
    if side == 1:
        count += 1

if n-count < count:
    minimalResult = n-count
else:
    minimalResult = count
print("Орлов: ", n-count, "Решек: ", count)

print("Минимальное количество монет, которые нужно перевернуть: ", minimalResult)


# Задача 12:
# Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.

# 4 4 -> 2 2
# 5 6 -> 2 3

# Решение______дискриминант__________

sum = int(input("Введите результат сложения чисел: "))
mul = int(input("Введите результат умноженич чисел: "))

D = sum * sum - 4 * mul
X = (sum + (D ** (0.5)))/2
Y = (sum - (D ** (0.5)))/2

print(X,Y)


# Задача 14:
# Требуется вывести все целые степени двойки (т.е. числавида 2k),
# не превосходящие числа N.

# 10 -> 1 2 4 8

# Решение 1_____________ответ в столбец_______________

N = int(input('Введите число N: '))
i = 1
while i<=N:
    print(i)
    i*=2



#Решение 2 Не работет ответ в строку
# N = int(input('Введите число N: '))
# j = 1
# k = 1
# length = 0
# while j<N:
#     length+=1
#     j*=2
# print(j)

# while k<N:
#     string = [k for i in range(3)]
#     print(string)
#     k*=2

# # string = [j for i in range(3)]
# # print(string)
# # N = int(input('Введите число N: '))
# # i = 0
# # coinSides = [random.randint(0,1) for i in range(n)]