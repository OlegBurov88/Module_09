# Пример создания простого декоратора
def null_decorator(func):
    return func


def greet():
    return 'Привет!'


print(greet())
greet = null_decorator(greet)
print(greet())

print()


# Можно использовать синтаксис Python для декорирования функции за один шаг
def null_decorator(func):
    return func


@null_decorator
def greet():
    return 'Hello!'


print(greet())

print()


# Почему нужно внутри декоратора определять ещё одну функцию
def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result

    return wrapper


@uppercase
def greet():
    return 'Здравствуйте!'


print(greet())

print()

import time
import sys


# Напишем функцию высшего порядка, на вход которой передается другая функция и параметры с которыми надо её вызвать
def time_track(func):
    def surrogate(*args, **kwargs):
        started_at = time.time()
        result = func(*args, **kwargs)
        ended_at = time.time()
        elapsed = round(ended_at - started_at, 4)
        print(f'Функция работала {elapsed} секунд(ы)')
        return result

    return surrogate


def digits(*args):
    total = 1
    for number in args:
        total *= number ** 5000
    return len(str(total))


sys.set_int_max_str_digits(100000)

result = digits(3141, 5926, 2718, 2818)
print(result)
print()

timed_digits = time_track(digits)
result = timed_digits(3141, 5926, 2718, 2818)
print(result)
print()

# а можно вообще сделать так
digits = time_track(digits)
result = digits(3141, 5926, 2718, 2818)
print(result)
# и теперь digits - почти та же функция, но не та. Она отдекорирована функцией time_track
# за счет *args, **kwargs внутренняя surrogate принимает все параметры
# и тут же передает их в декорируемую функцию
