import sys
from itertools import repeat

ex_itertator = repeat('4', 100_000)
print(ex_itertator)
print(f'Размер итератора: {sys.getsizeof(ex_itertator)}')

ex_str = '4' * 100_000
print(f'Размер списка: {sys.getsizeof(ex_str)}')

print()


# Что же это за зверь такой - итератор?
#
# В python можно проходить циклом по любому обьекту, если он - итерируемый.
# А что бы обьект стал итерируемым, он должен содержать два метода - __iter__ и __next__


class Iter:

    def __init__(self):
        self.first = 'Первый элемент'
        self.second = 'Второй элемент'
        self.third = 'Третий элемент'
        self.i = 0

    def __iter__(self):
        # обнуляем счетчик перед циклом
        self.i = 0
        # возвращаем ссылку на себя - я буду итератором!
        return self

    def __next__(self):
        # а этот метод возвращает значения по требованию python
        self.i += 1
        if self.i == 1:
            return self.first
        if self.i == 2:
            return self.second
        if self.i == 3:
            return self.third
        if self.i == 4:
            return f'Подсчёт окончен.'
        raise StopIteration()  # признак того, что больше возвращать нечего


obj = Iter()
print(obj)
for value in obj:
    print(value)

# То есть интерпретатор вызывает метод __next__ при каждом проходе цикла
# а если в __next__ возникает исключение StopIteration - то значит в обьекте нет больше элементов
# и цикл прекращается

print()

# Еще пример: последовательность Фибоначчи - https://goo.gl/PoqS7
# Последовательность, в которой каждое последующее число равно сумме двух предыдущих чисел:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, ...
def fibonacci(n):
    result = []
    a, b = 0, 1
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result


for value in fibonacci(n=10):
    print(value)
# Для больших N функция создаст в памяти огромный список и вернет его - нерационально!

print()

# Сделаем итератор, который будет вычислять следующее значение по требованию (lazy evaluation https://goo.gl/7fzXuA)
class Fibonacci:
    """Итератор последовательности Фибоначчи до N элементов"""

    def __init__(self, n):
        self.i, self.a, self.b, self.n = 0, 0, 1, n

    def __iter__(self):
        self.i, self.a, self.b = 0, 0, 1
        return self

    def __next__(self):
        self.i += 1
        if self.i > 1:
            if self.i > self.n:
                raise StopIteration()
            self.a, self.b = self.b, self.a + self.b
        return self.a


fib_iterator = Fibonacci(10000)
print(fib_iterator)
for value in fib_iterator:
    print(value)
print(13 in fib_iterator)
# Каждое значение вычисляется "по месту" - тогда, когда оно понадобилось.
