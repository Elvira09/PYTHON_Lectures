## Ускоренная обработка данных:
	# lambda, filter, map, zip, 
	# enumerate, lst Comprehension

# Функции
print('Функции')

def f(x):
	return x ** 2
print(f(2))			# 4

g = f
print(type(f))		# <class 'function'>
print(g(2))			# 4

def calc1(x):
	return x + 10
print(calc1(10))	# 20

def calc2(x):
	return x * 10
print(calc2(10))	# 100

def math(op, x):
	print(op(x))
math(calc1, 10)		# 20
math(calc2, 10)		# 100

def sum(x, y):
	return x + y

def mylt(x, y):
	return x * y

def calc(op, a, b):
	print(op(a, b))		
	# return op(a, b)

calc(mylt, 4, 5)	# 20
f = sum
calc(f, 4, 5)	# 9

# Анонимные lambda функции
print('\nАнонимные lambda функции')
# def sum(x, y):
# 	return x + y
# аналог 
sum = lambda x, y: x + y
print(sum)	# <function <lambda> at 0x104c629e0>

calc(sum, 8, 9)	# 17
calc(lambda x, y: x + y, 8, 9)	# 17

# lst Comprehension
	# [exp for item in iterable]
	# [exp for item in iterable (if conditional)]
	# [exp <if conditional> for item in iterable (if conditional)]
print('\nlst Comprehension')

lst = []
for i in range(1, 21):
	if i % 2 == 0:
		lst.append(i)
print(lst)		# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# аналогичная запись с помощью lst Comprehension
lst = [i for i in range(1, 21) if i % 2 == 0]
print(lst)		# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

def f(x):
	return x ** 2

lst = [f(i) for i in range(1, 21) if i % 2 == 0] # действия с элементами
print(lst)	# [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]
#список картежей
lst = [(i, i) for i in range(1, 21) if i % 2 == 0]
print(lst)	#  [(2, 2), (4, 4), (6, 6), (8, 8), (10, 10), (12, 12), (14, 14), (16, 16), (18, 18), (20, 20)]

lst = [(i, f(i)) for i in range(1, 21) if i % 2 == 0] # можно так же вместо f(i) записать (i, i**2)
print(lst)	# [(2, 4), (4, 16), (6, 36), (8, 64), (10, 100), (12, 144), (14, 196), (16, 256), (18, 324), (20, 400)]

# Задача
print('\nЗадача')

path = 'Lect03_file.txt'
d = open(path, 'r')
data = d.read() + ' '
d.close()

num = []
while data != '': # проверка пока строка не пустая
	pos = data.index(' ') # находим первую позицию пробела
	num.append(int(data[:pos]))
	data = data[pos+1:]

out = []
for i in num:
	if not i % 2: # равносильно i % 2 == 0
		out.append((i, i**2))
print(out)		# [(2, 4), (8, 64), (38, 1444)]


def select(f, col):
 	return [f(x) for x in col]
def where(f, col):
 	return [x for x in col if f(x)]

data = '1 2 3 5 8 15 23 38'.split()
res = select(int, data)
res = where(lambda x: not x % 2, res)
res = list(select(lambda x: (x, x**2), res))
print(res)		# [(2, 4), (8, 64), (38, 1444)]

# Функция map() применяет указанную функцию к
# каждому элементу итерируемого объекта и
# возвращает итератор с новыми объектами
# ! Нельзя пройтись дважды
print('\nФункция map()')

li = [x for x in range(1, 20)]
li = list(map(lambda x: x + 10, li))
print(li)	# [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]

# data = list(map(int, input().split()))
data = list(map(int, '1 2 3 5 8 15 23 38'.split()))
print(data)		# [1, 2, 3, 5, 8, 15, 23, 38]

data = '1 2 3 5 8 15 23 38'.split()
res = map(int, data)
res = where(lambda x: not x % 2, res)
res = list(map(lambda x: (x, x**2), res))
print(res)		# [(2, 4), (8, 64), (38, 1444)]

# Функция filter() применяет указанную функцию к
# каждому элементу итерируемого объекта и
# возвращает итератор с теми объектами, для
# которых функция вернула True.
# ! Нельзя пройтись дважды
print('\nФункция filter()')

data = [x for x in range(10)]
res = list(filter(lambda x: not x % 2, data))
print(res)	# [0, 2, 4, 6, 8]

data = '1 2 3 5 8 15 23 38'.split()
res = map(int, data)
res = filter(lambda x: not x % 2, res)
res = list(map(lambda x: (x, x**2), res))
print(res)	# [(2, 4), (8, 64), (38, 1444)]

# # Функция zip() применяется к набору итерируемых
# # объектов и возвращает итератор с кортежами из
# # элементов входных данных.
# # Количество элементов в результате равно минимальному 
# # количеству элементов входного набора 
# # ! Нельзя пройтись дважды
print('\nФункция zip()')

users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]

data = list(zip(users, ids))
print(data)	# [('user1', 4), ('user2', 5), ('user3', 9), ('user4', 14), ('user5', 7)]

salary = [111, 222, 333,]
data = list(zip(users, ids, salary))
print(data)		# [('user1', 4, 111), ('user2', 5, 222), ('user3', 9, 333)]

# # Функция enumerate() применяется к итерируемому
# # объекту и возвращает новый итератор с кортежами
# # из индекса и элементов входных данных.
# # ! Нельзя пройтись дважды
print('\nФункция enumerate()')

data = list(enumerate(users))
print(data)	# [(0, 'user1'), (1, 'user2'), (2, 'user3'), (3, 'user4'), (4, 'user5')]




# def sum(x):
#  	return x+10
# def mult(x):
#  	return x**2
# #сокращаем функции
# sum = lambda x: x+10
# mult = lambda x: x**2
# sum(mult(2))

# sum1 = lambda x: x+22
# mult2 = lambda x: x**3
# sum1(mult2(2))

# sum4 = lambda x: x+242
# mult4 = lambda x: x**5
# sum3(mult2(2))

