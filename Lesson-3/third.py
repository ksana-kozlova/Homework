# Написать функцию, которая будет принимать только 4 позиционных аргументы (все аргументы числовые).
# Функция должна вернуть среднее арифметическое аргументов и самый большой аргумент за все время вызовов этой функции.
import sys
maximum = -sys.maxsize - 1


def aver_and_max(a: (int, float), b: (int, float), c: (int, float), d: (int, float)):
    global maximum
    maximum = max(max(a, b, c, d), maximum)
    return (a + b + c + d) / 4, maximum


print(aver_and_max(1, 2, 3, 4))
print(aver_and_max(1, 2, 5, 4))