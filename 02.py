## Данные, функции и модули в python
# Файлы

# Как работать с файлами:
# Связать файловую переменную с файлом,
# определив модификатор работы
	# a – открытие для добавления данных
	# r – открытие для чтения данных
	# w – открытие для записи данных
	# w+, r+

print('Файлы')
	# запись данных в файл
		# Вариант 1
colors = ['red', 'green', 'blue123']
data = open('Lect02_file.txt', 'a')
data.writelines(colors) # разделителей не будет
data.write(('\nLINE 12 \n'))
data.write(('LINE 13 \n'))
data.close()

		# Вариант 2
with open('Lect02_file.txt', 'a') as data:
 	data.write('line 1\n')
 	data.write('line 2\n')

	# Чтение данных из файла В КОНСОЛИ
path = 'Lect02_file.txt'
data = open(path, 'r')
for line in data:
	print(line)
data.close()


# #   Функции и модули
print('\nФункции и модули')

# import function_file # название файла с функцией
# import function_file as ff # сокращение названия файла для дальнейшего обращения 

def new_string(symbol, count):
	return symbol * count
print(new_string('!', 5)) # !!!!!
# print(new_string('!')) # TypeError missing 1 required ...

def new_string(symbol, count = 3):
 	return symbol * count
print(new_string('!', 5)) # !!!!!
print(new_string('!')) # !!!
print(new_string(4)) # 12

# !для передачи неограниченного числа аргументов функции ставиться '*'
def concatenatio(*params):
	res: str = ""
	for item in params:
		res += item
	return res
print(concatenatio('a', 's', 'd', 'w')) # asdw
print(concatenatio('a', '1', 'd', '2')) # a1d2
# print(conatenatio(1, 2, 3, 4)) # TypeError: ...


## Рекурсия
print('\nРекурсия')

def fib(n): # ряд фибоначи
	if n in [1, 2]:
		return 1
	else:
		return fib(n-1) + fib(n-2)

list = []
for e in range(1, 10):
	list.append(fib(e))
print(list) # 1 1 2 3 5 8 13 21 34


# # Кортежи
# # Кортеж – это неизменяемый “список”
print('\nКортежи')

a = (3, 4, 7, 9)
print(a)  		# (3, 4, 7, 9)
print(a[0])		# 3
print(a[-1])	# 9

t = ()
print(type(t)) # tuple
t = (1,)
print(type(t)) # tuple
t = (1)
print(type(t)) # int
t = (28, 9, 1990)
print(type(t)) # tuple
colors = ['red', 'green', 'blue']
print(colors) # ['red', 'green', 'blue']
t = tuple(colors)
print(t) # ('red', 'green', 'blue')


t = tuple(['red', 'green', 'blue'])
print(t[0]) # red
print(t[2]) # blue
# print(t[10]) # IndexError: tuple index out of range
print(t[-2]) # green
# print(t[-200]) # IndexError: tuple index out of range
for e in t:
	print(e) # red green blue
# t[0] = 'black' # TypeError: 'tuple' object does not support item assignment

t = tuple(['red', 'green', 'blue'])
red, green, blue = t
print('r:{} g:{} b:{}'.format(red, green, blue)) # r:red g:green b:blue


# # Словари - Неупорядоченные коллекции произвольных
# # объектов с доступом по ключу
print('\nСловари')

dictionary = {}
dictionary = \
	{
 		'up': '↑',
		'left': '←',
		'down': '↓',
		'right': '→'
 	}
print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
print(dictionary['left']) # ←
# типы ключей могут отличаться

for k in dictionary.keys(): # доступ ко всем ключам
	print(k) 	# up left down right

for v in dictionary.values(): # доступ ко всем значениям
	print(v)	# ↑ ← ↓ →

print(dictionary['up']) # ↑
dictionary['left'] = '⇐'
print(dictionary['left']) # ⇐
#print(dictionary['type']) # KeyError: 'type'
del dictionary['left'] # удаление элемента
for item in dictionary: # for (k,v) in dictionary.items():
	print('{}: {}'.format(item, dictionary[item]))
		# up: ↑
		# down: ↓
		# right: →


# # Множества - Неупорядоченная совокупность элементов
print('\nМножества')

colors = {'red', 'green', 'blue'}
print(colors) 		# {'red', 'green', 'blue'}
# добаление элементов
colors.add('red')
print(colors) 		# {'red', 'green', 'blue'}
colors.add('gray')
print(colors) 		# {'red', 'green', 'blue','gray'}
# удаление элементов
colors.remove('red')
print(colors) 		# {'green', 'blue','gray'}
# colors.remove('red') # KeyError: 'red'
colors.discard('red') # ok
print(colors) 		# {'green', 'blue','gray'}
# очистка множества
colors.clear() 		# { }
print(colors) 		# set()

a = {1, 2, 3, 5, 8}
b = {'2', '5', 8, 13, 21}
print(type(a)) # set
print(type(b)) # set

a = {1, 2, 3, 5, 8}
b = set([2, 5, 8, 13, 21])
c = set((2, 5, 8, 13, 21))
print(type(a)) # set
print(type(b)) # set
print(type(c)) # set
a = {1, 1, 1, 1, 1}
print(a) # {1}

a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
# копирование множества
c = a.copy() 			# c = {1, 2, 3, 5, 8}
# объединение множества
u = a.union(b) 			# u = {1, 2, 3, 5, 8, 13, 21}
# пересечение множества
i = a.intersection(b) 	# i = {8, 2, 5}
# вычитание / разница
dl = a.difference(b) 	# dl = {1, 3}
dr = b.difference(a) 	# dr = {13, 21}

q = a \
 .union(b) \
 .difference(a.intersection(b)) # {1, 21, 3, 13}

# Неизменяемое множество
a = {1, 2, 3, 5, 8}
b = frozenset(a)
print(b) # frozenset({1, 2, 3, 5, 8})

# СПИСКИ
print('\nСписки')

list1 = [1, 2, 3, 4, 5]
list2 = list1 # при таком копировании изменение элементов в любом из списков будут отражаться и на втором
print(list1)
print(list2)

for i in list1:
	print(i)
print()
for i in list2:
	print(i)

list1[0] = 123
list2[1] = 333

print(list1)
print(list2)

# удаление последнего элемента
list1 = [1, 2, 3, 4, 5]
print(list1)
print(list1.pop())
print(list1)
print(list1.pop())
print(list1)
# добавление элемента на указанную позицию
print(list1.insert(2, 11)) #2 - индекс, 11 - элемент
print(list1)
# добавление элемента в конец
print(list1.append(15)) 
print(list1)			



