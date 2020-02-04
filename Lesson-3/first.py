# Написать несколько функций, которые в качестве единственного аргумента принимают список (или кортеж) целых чисел.
# - первая функция должна вернуть квадраты элементов коллекции;
# - вторая функция должна вернуть только элементы на четных позициях;
# - третья функция возвращает кубы четных элементов на нечетных позициях.


def foo_one(a: 'tuple or list of int'):
    b = list(map(lambda element: element ** 2, a))
    return b


def foo_two(a: 'tuple or list of int'):
    b = [v for k, v in enumerate(a) if k % 2]
    return b


def foo_three(a: 'tuple or list of int'):
    b = [v**3 for k, v in enumerate(a) if not k % 2]
    return b

