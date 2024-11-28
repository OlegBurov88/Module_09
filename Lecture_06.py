def func_generator(n):
    i = 0
    while i != n:
        yield i
        i += 1


obj = func_generator(10)
print(obj)

for i in obj:
    print(i)

print()


# А теперь поймаем за хвост другого зверя - генератора.
#
# Мы видели генераторные сборки, но обычную функцию тоже можно превратить в генератор.


def fibonacci_v1(n):
    result = []
    a, b = 0, 1
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result


# Как уже говорили - нерационально: в памяти создается большой список...
# Решение  - оператор yield (производить, выдавать значение)


# Он приостанавливает выполнение функции и ждет следующего вызова __next__
# и функция превращается в генератор
def fibonacci_v2(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


fib_1 = fibonacci_v1(n=10)
print(fib_1)

print()

for value in fib_1:
    print(value)

print()

fib_2 = fibonacci_v2(n=10)
print(fib_2)
for value in fib_2:
    print(value)

for i in fib_2:
    print(i)

print()


# Можно вообще сделать бесконечный "список" значений
def fibonacci_v3():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


for value in fibonacci_v3():
    print(value)
    if value > 10 ** 6:
        break

print()


# В генераторах можно использовать return - он воспринимается, как завершение итерирования
# и аналогичен raise StopIteration()
def fibonacci_v4():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
        if a > 10 ** 30:
            return


for val in fibonacci_v4():
    print(val)
# Если у return есть значение, оно помещается в StopIteration - то есть _практически_ не видимо снаружи
