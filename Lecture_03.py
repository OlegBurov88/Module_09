# Ленивые вычисления - это когда значения вычисляются при необходимости
# Это делают генераторные сборки
import time

my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
result = (x ** 100 for x in my_numbers)
print(result)
for elem in result:
    print(elem)

print()

# прочитать генераторную сборку можно лишь один раз
my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
result = (x ** 1000 for x in my_numbers)
for elem in result:
    print(elem)
print('Еще разок')
for elem in result:
    print(elem)

print()


start_time = time.time()

my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
result = [x ** 3000 for x in my_numbers]
for elem in result:
    print(elem)

finish_time = time.time()
print(f'Время в миллисекундах: {(finish_time-start_time)*1000}мс')

print()

start_time = time.time()

my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
result = (x ** 3000 for x in my_numbers)
for elem in result:
    print(elem)

finish_time = time.time()
print(f'Время в миллисекундах: {(finish_time-start_time)*1000}мс')

print()

# используются там, где надо производить затратные операции
my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
result = (x ** 3 for x in my_numbers)
for i in result:
    print(i)
    if str(i).startswith('100'):
        break
# обратите внимание, что числа 9, 2, 6 не возводились в степень - профит!
print()
# Многие функции в пайтоне - ленивые. Например: map, filter, range и т.д.
# Вот почему мы оборачивали их вызовы в list() - при этом генератор все таки работает и создает список в памяти

list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]

ran = range(10, 30)
zp = zip(list_1, list_2)
mp = map(str, list_1)

print(ran, zp, mp)

print(list(ran))
print(list(zp))
print(list(mp))