'''Каррирование.
  Преобразовать вызов функции с конечным количеством позиционных аргументов f(a, b, c, d) в вызов вида f(a)(b)(c)(d), используя декоратор.
  Пример:
  @carry
  def foo(a, b):
        return a + b

   foo(1)(5)  # вернет 6'''
from functools import partial


def carry(function):

    def wrapped(*args):
        if len(args) >= function.__code__.co_argcount:
            return function(*args)
        return partial(wrapped, *args)

    return wrapped


@carry
def foo(a, b, c):
    return a + b + c


print(foo(1)(5)(3))  # вернет 9