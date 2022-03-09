# Типы данных и переменная
# int, float, boolean, str, list, None
print('\nТипы данных и переменная int, float, boolean, str, list, None')

#type - показывает тип переменной

value = None
print(value, ' - ', type(value)) # None

a = 123
print(a, ' - ', type(a)) 	# int

b = 1.23
print(b, ' - ', type(b))	# float 

value = 12334
print(value, ' - ', type(value)) # int

s = 'hello world' 
print(s, ' - ',  type(s))	# str

f = True
print(f, ' - ', type(f))	# bool

list1 = [1, 2, 3] 
print(list1, ' - ', type(list1))	# list

col = ['hello', 1, 3, 4.5, True]
print(col, ' - ', type(col))	# list

# варианты выводов
# \n - переход на другую строку
print('\nварианты выводов')

print(a, b, s)
print(a, '-', b, '-', s)
print('{} - {} - {}'.format(a, b, s))
print('{2} - {0} - {1}'.format(a, b, s)) #в скобках проставляем индексы
print(f'{a} - {b} - {s}') #в данном случае после скобки необходима буква f


# Ввод и вывод данных
# print - вывод, input - ввод
print('\nВвод и вывод данных print, input')

print('Введите a')
a1 = input()
print('Введите b')
b1 = input()
print(a1, '+', b1, '=', a1+b1, ' - итогом a+b будет просто сращивание чисел') #в данном случает итогом a+b будет просто сращивание чисел
print('{} {}'.format(a1, b1))
print(f'{a1} {b1}')

print('Введите a')
a1 = int(input())
print('Введите b')
b1 = int(input())
#в данном случает итогом a+b будет арифметическое действие, т.к. простаивли тип переменной int(можно float)
print(a1, '+', b1, '=', a1+b1, '  - итогом a+b будет арифметическое действие') 

# Арифметические операции 
# +, -, *, /, %, //,**
# Приоритет операций
# **, ⊕, ⊖, *, /, //, %, +, -
# ( ), Сокращенные операции присваивания
	# // - результат деления - целое число
	# ** - возведение в степень
	# % - остаток от деления
print('\nАрифметические операции')

a = 12
b = 8
c = a / b
print(f'{a}', '/', f'{b}', '=', c, ' - результат точный')
c = a // b
print(f'{a}', '//', f'{b}', '=', c, ' - результат целое число')
c = a % b
print(f'{a}', '%', f'{b}', '=', c, ' - остаток от деления')
c = a ** b
print(f'{a}', '**', f'{b}', '=', c, ' - возведение в степень')

a = 1.667
b = 8.895
#функция round округляет до указанного кол-ва знаковю если кол-во не указанао - до целого числаb = 8
c = round(a * b) 
print(f'{a}', '*', f'{b}', '=', c, ' - результат целое число')
c = round(a * b, 5) # округляем результат до 5 знаков после запятой
print(f'{a}', '*', f'{b}', '=', c, ' - результат с 5 знаками после запятой')


# Логические операции
# >, >=, <, <=, ==, !=
# not, and, or – не путать с &, |, ^
# is, is not, in, not in
# gen
print('\nЛогические операции')

a = 1 > 3
print(a, '  # a = 1 > 3')
a = 1 < 4 and 5 > 2
print(a, '  # a = 1 < 4 and 5 > 2')
a = 'hello'
b = 'hello'
print(a == b, '  # a == b, a = hello, b = hello')
a = [1, 5, 3]
b = [1, 3, 5]
print(a == b, '  # a == b, a = [1, 5, 3], b = [1, 3, 5]')

func = 1
t = 4
x = 123
print(func < t > x, '  # func < t > x, func = 1, t = 4, x = 123')
f = 1 > 2 or 4 < 6
print(f, '  # f = 1 > 2 or 4 < 6')
f = [5, 4, 6, 2]
print(6 in f, f, '  # 6 - проверяем наличие в списке') 
is_odd = not f[0] % 2 > 0
print(is_odd, '  # f[0] % 2 > 0' )

# Управляющие конструкции:
# if, if-else
print('\nУправляющие конструкции: if, if-else')

a = int(input('a = '))
b = int(input('b = '))
if a > b:
	print(a, '  #', f'{a}', ' > ', f'{b}')
else:
	print(b, '  #', f'{a}', ' < ', f'{b}')

username = input('Представьтесь ')
if username == 'Маша':
	print('Здравствуй, Маша!')
elif username == 'Марина':
	print('О, Марина!')
elif username == 'Вася':
	print('Как дела, Василий?')
else:
	print('Привет, ', username)


# Управляющие конструкции:
# while, while-else
print('\nУправляющие конструкции: while, while-else')

original = 23
inverted = 0
while original !=0:
	inverted = inverted * 10 + (original % 10)
	original //= 10
else:
	print('Пожалуй хватит ')
print(inverted, ' # инвертируемое число ')


# Управляющие конструкции:
# for
print('\nУправляющие конструкции: for')

list2 = [1, 4, 6, 2]
for i in list2:
	print(i ** 2)

# функция range показывает по порядку цифры элемента
r = range(5, 20, 4) # от 5 до 20 с шагом 4
print('Показать числа от 5 до 20 с шагом 4')
for i in r:
	print(i)

s = 'hello'
print(s)
for i in s:
	print(i)

# Строки
print('\nСтроки')

text = 'съешь ещё этих мягких французских булок'
print(len(text), ' - длина строки') # 39 
print('ещё' in text) # True
print(text.isdigit()) # False
print(text.islower()) # True
print(text.replace('ещё','ЕЩЁ')) #
for c in text:
	print(c)

print(text[0]) # c
print(text[1]) # ъ
print(text[len(text)-1]) # к
print(text[-5]) # б
print(text[:]) # print(text)
print(text[0:2]) # съ
print(text[len(text)-2:]) # ок
print(text[2:9]) # ешь ещё
print(text[6:-18]) # ещё этих мягких
print(text[0:len(text):6]) # сеикакл
print(text[::6]) # сеикакл
text = text[2:9] + text[-5] + text[:2] # ...


# СПИСКИ
#  list = list
print('\nСПИСКИ')

numbers = [1, 2, 3, 4, 5]
print(numbers) 
ran = range(1, 8)
print(type(ran))
numbers = list(ran)
print(numbers, ' # [1, 2, 3, 4, 5, 6, 7]') 
numbers[0] = 10
print(numbers) # заменяем  первый элемент

for i in numbers: # умножаем каждый элемент на 2
 	i *= 2
 	print(i) # [20, 4, 6, 8, 10]
print(numbers, ' # возвращается изначальный список') # [10, 2, 3, 4, 5] 

colors = ['red', 'green', 'blue']
for e in colors:
 	print(e) # red green blue
for e in colors:
 	print(e*2) # redred greengreen blueblue
colors.append('gray') # добавить в конец
print(colors == ['red', 'green', 'blue', 'gray']) # True
colors.remove('red') #del colors[0] # удалить элемент


#  ФУНКЦИИ
print('\nФУНКЦИИ')

def f(x):
 	if x == 1:
 		return 'Целое'
 	elif x == 2.3:
 		return 23
 	else:
 		return

arg = 1
print(f(arg), type(f(arg))) 
arg = 2.3
print(f(arg), type(f(arg))) 
arg = 2
print(f(arg), type(f(arg))) 




