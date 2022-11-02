# print('hello world')

# Переменные
# типы данных
# int, float, boolean, str, list, None
# value = None
# 
# print(type(a))
# print(type(b))
# value = 12345
# print(type(value))
# a = 123
# b = 1.23
# s = 'hello world'
# print(s) # вывод строки
# print(a, '-', b, '-', s)
# print('{} - {} - {}'.format(a, b, s))
# print(f'{a} - {b} - {s}')
# print('{1} - {2} - {0}'.format(a, b, s))

# f = True
# print(f) # логические переменные
# list = ['1', '2', '3', 'hello', 1, 2, 4.5, True]
# print(list)

# print('Введите а')
# a = float(input())
# print('Введите b');
# b = float(input())
# print(a, ' + ', b, ' = ', a+b)
# print('{} {}'.format(a, b))
# print(f'{a} {b}')

# Арифметические операции
# +, -, * , /, %, //, **
# Приоритет операций
# ** , ⊕, ⊖, * , /, //, %, +, -
# ( ) Скобки меняют приоритет

# a = 1.3236
# b = 3
# c = round(a * b, 3)
# print(c)

# Сокращённые операции и операции присваивания

# iter = 2
# iter += 3 # iter = iter + 3
# iter -= 4 # iter = iter - 4
# iter *= 5 # iter = iter * 5
# iter /= 5 # iter = iter / 5
# iter //= 5 # iter = iter // 5
# iter %= 5 # iter = iter % 5
# iter **= 5 # iter = iter ** 5

# Логические операции
# >, >=, <, <=, ==, !=
# not, and, or – не путать с &, |, ^
# is, is not, in, not in

# a = 1 < 4 and 5 > 2
# print(a)

# f = 1 > 2 or 4 < 6
# print(f)

# f = [1, 2, 3, 4]
# print(f)
# print(not 2 in f)

# is_odd = not f[0] % 2 # или f[0] % 2 == 0 (но это хуже)
# print(is_odd)

# Конструкции ветвления if и else


# a = int(input('a = '))

# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)

# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же МАША!')
# elif username == 'Марина':
#     print('Я так ждала Вас, Марина!')
# elif username == 'Ильнар':
#     print('Ильнар - топ)')
# else:
#     print('Привет, ', username)

# Конструкция цикла while

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
#     print(original)
# else:
#     print('Пожалуй')
#     print('хватит )')
# print(inverted)

# Конструкция цикла for

# r = range(5) # range(0, 5)
# r = range(2, 5) # range(2, 5)
# r = range(-5, 0) # range(-5, 0)
# r = range(1, 10, 2) # range(1, 10, 2)
# r = range(100, 0, -20) # range(100, 0, -20)


# r = range(1, 10, 2)
# for i in r:
#     print(i)

# for i in 'qwerty':
#     print(i)

#Строки

text = 'съешь ещё этих мягких французских булок'
# # print(len(text)) # 39
# # print('ещё' in text) # True
# # print(text.isdigit()) # False
# # print(text.islower()) # True
# # print(text.replace('ещё','ЕЩЁ')) #
for c in text:
 print(c)

# text = 'съешь ещё этих мягких французских булок'
# print(text[0]) # c
# print(text[1]) # ъ
# print(text[len(text)-1]) # к
# print(text[-5]) # б
# print(text[:]) # print(text)
# print(text[:2]) # съ
# print(text[len(text)-2:]) # ок
# print(text[2:9]) # ешь ещё
# print(text[6:-18]) # ещё этих мягких
# print(text[0:len(text):6]) # сеикакл
# print(text[::6]) # сеикакл
# text = text[2:9] + text[-5] + text[:2] # ..
# # help(text.isalpha)

# Списки: введение

# Список – пронумерованная, изменяемая коллекция объектов произвольных типов

# numbers = [1, 2, 3, 4, 5]
# print(numbers) # [1, 2, 3, 4, 5]

# numbers = list(range(1, 6))
# print(numbers) # [1, 2, 3, 4, 5]

# numbers[0] = 10
# print(numbers) # [10, 2, 3, 4, 5]

# for i in numbers:
#  i *= 2
#  print(i) # [20, 4, 6, 8, 10]
# print(numbers) # [10, 2, 3, 4, 5]


# colors = ['red', 'green', 'blue']

# for e in colors:
#  print(e) # red green blue

# for e in colors:
#  print(e*2) # redred greengreen blueblue

# colors.append('gray') # добавить в конец
# print(colors == ['red', 'green', 'blue', 'gray']) # True
# colors.remove('red') #del colors[0] #
# print(colors)


# Функции

# def f(x):
#     if x == 1:
#         return 'Целое'
#     elif x == 2.3:
#         return 23
#     else:
#         return
# arg = 1
# print(f(arg))
# # print(type(f(arg)))
