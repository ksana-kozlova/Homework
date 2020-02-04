# Написать функцию, которая принимает произвольное количество любых аргументов.
# Аргументами могут быть вложенные списки и кортежи, содержащие числа и другие списки и кортежи.
# Пример вызова функции: foo(1, 2, [3, 4, (5, 6, 0)], a=(10, 11), b=(3, 4, [5, 6, [7, 8], []]))
# Функция должна вернуть произведение и сумму всех ненулевых элементов вложенных чисел.
# Возможны циклические ссылки в аргументах. Пример такого аргумента: a = [1, 2, 3]; a.append(a)
# При обнаружении циклической ссылки нужно сообщить пользователю и вернуть None.


def sum_and_mult(*args: (list, tuple), **kwargs: (list, tuple)):
    total_sum = 0
    total_mult = 1

    def s_and_m(*args: (list, tuple), **kwargs: (list, tuple)):
        nonlocal total_sum, total_mult
        for x in args:
            if isinstance(x, (list, tuple)):
                s_and_m(*x)
            elif x != 0:
                total_sum += x
                total_mult *= x
        for x in kwargs:
            if isinstance(kwargs[x], (list, tuple)):
                s_and_m(*kwargs[x])
            elif kwargs[x] != 0:
                total_sum += kwargs[x]
                total_mult *= kwargs[x]
    s_and_m(*args, **kwargs)
    return total_sum, total_mult


print(sum_and_mult(1, 2, [3, 4, (5, 6, 0)], a=(10, 11), b=(3, 4, [5, 6, [7, 8], []])))