# Задача 16: Требуется вычислить, сколько раз встречается некоторое 
# число X в массиве A[1..N]. Пользователь в первой строке вводит 
# натуральное число N – количество элементов в массиве. В последующих  
# строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1



# import random

# num = int(input("Введите количество элементов массива: "))
# array = []
# for i in range(num):
#     array.append (random.randint(0, 9))
# print(array)
# x = int(input("Введите число Х: "))
# amount = 0
# for i in range(len(array)):
#     if array[i] == x:
#         amount += 1
   
# print(amount)






# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине 
# элемент к заданному числу X. Пользователь в первой строке вводит 
# натуральное число N – количество элементов в массиве. В последующих  
# строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

#  хз, как найти приближенное число

# import random

# num = int(input("Введите количество элементов массива: "))
# array = []
# for i in range(num):
#     array.append (random.randint(0, 9))
# print(array)

# x = int(input("Введите число: "))
# similar = 0
# for i in array:
#     if i == x-1:
#         similar = i
            
# if similar == 0:
#     print("заданному элементу Х не соответствует условие задачи")
# else:
#     print(f"самый близкий по величине элемент к '{x}' это '{similar}' ")





# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет 
# определенную ценность. В случае с английским алфавитом очки распределяются 
# так:A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; B, C, M, P – 3 очка; 
# F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков. А русские 
# буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка; 
# Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; 
# Ф, Щ, Ъ – 10 очков. Напишите программу, которая вычисляет стоимость введенного 
# пользователем слова. Будем считать, что на вход подается только одно слово, которое 
# содержит либо только английские, либо только русские буквы.

# *Пример:*

# ноутбук
#     12

t1 = ("A", "E", "I", "O", "U", "L", "N", "S", "T", "R", "А", "В", "Е", "И", "Н", "О", "Р", "С", "Т",)
t2 = ("D", "G", "Д", "К", "Л", "М", "П", "У",)
t3 = ("B", "C", "M", "P", "Б", "Г", "Ё", "Ь", "Я",)
t4 = ("F", "H", "V", "W", "Y", "Й", "Ы",)
t5 = ("K", "Ж", "З", "Х", "Ц", "Ч",)
t8 = ("J", "X", "Ш", "Э", "Ю",)
t10 = ("Q", "Z", "Ф", "Щ", "Ъ",)

text = str(input("Введите слово: "))
word = text.upper()
counter = 0
for i in word:
    if i in t1:
        counter += 1
    elif i in t2:
        counter += 2
    elif i in t3:
        counter += 3
    elif i in t4:
        counter += 4
    elif i in t5: 
        counter += 5
    elif i in t8:
        counter += 8
    elif i in t10:
        counter +=10
print(counter)