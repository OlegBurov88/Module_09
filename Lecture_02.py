# Синтаксический сахар - списковые сборки

def by_3(x):
    return x * 3


def is_odd(x):
    return x % 2


my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
result = map(by_3, filter(is_odd, my_numbers))
print(list(result))
# выглядит не очень понятно

print()

my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
result = map(lambda x: x * 3, filter(lambda x: x % 2, my_numbers))
print(list(result))
# так лучше, но все равно много знаков препинания, скобок, ключевых слов...

print()

# списковая сборка - один список создается на лету из другого - аналог map
my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
result = [x * 3 for x in my_numbers]
print(result)

# аналог filter
my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
result = [x for x in my_numbers if x % 2]
print(result)

# и совмещение обоих способов
my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
result = [x * 3 for x in my_numbers if x % 2]
# ср. map(lambda x: x * 3, filter(lambda x: x % 2, my_numbers))
print(result)

print()

my_numbers = ['A', 1, 4, 'B', 5, 'C', 2, 6]
result = [x if type(x) == str else x * 5 for x in my_numbers]
print(result)

print()

# можно делать вложенные циклы
my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
they_numbers = [2, 7, 1, 8, 2, 8, 1, 8]
result = [x * y for x in my_numbers for y in they_numbers]
print(result)
result = [x * y for x in my_numbers for y in they_numbers if x % 2]
print(result)
result = [x * y for x in my_numbers for y in they_numbers if x % 2 and y // 2]
print(result)

print()

# Так же можно создавать на лету множества
my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
result = {x for x in my_numbers}
print(result)
# обратите внимание на упорядоченность и отсутсвие повторяющихся элементов

print()

# и словари
my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
result = {x: x ** 2 for x in my_numbers}
print(result)

print()

# Ленивые вычисления - это когда значения вычисляются при необходимости
# Это делают генераторные сборки
my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
result = (x ** 10 for x in my_numbers)
print(result)
for elem in result:
    print(elem)

print()

# прочитать генераторную сборку можно лишь один раз
my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
result = (x ** 10 for x in my_numbers)
for elem in result:
    print(elem)
print('Еще разок')
for elem in result:
    print(elem)

print()

# используются там, где надо производить затратные операции
my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
result = (x ** 30 for x in my_numbers)
for i in result:
    print(i)
    if str(i).startswith('100'):
        break
# обратите внимание, что числа 9, 2, 6 не возводились в степень - профит!

# Многие функции в пайтоне - ленивые. Например: map, filter, range и т.д.
# Вот почему мы оборачивали их вызовы в list() - при этом генератор все таки работает и создает список в памяти
