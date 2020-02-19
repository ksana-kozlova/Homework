'''2. Напишите параметризованный декоратор для классов,
 который будет считать и выводить время работы методов класса, имена которых переданы в параметрах декоратора.
Пример:
  @time_methods('inspect', 'finalize')
  class Spam:
      def __init__(self, s):
          self.s = s
      def inspect(self):
           sleep(self.s)
      def foo(self):
           return self.s

 a = Spam(2)
 a.inspect()  #  должно вывести сообщение о времени работы
 a.foo()  # ничего не выводить'''




from time import time, sleep
from functools import wraps

"Я пыталась, но это не работает"
def time_methods(*methods):
    def inner_decorator(cls):
        getattribute = cls.__getattribute__
        @wraps(cls)
        def wrapper(*args, **kwargs):
            for (key, value) in getattribute:
                if key in args:
                    current_time = time()
                    value
                    result = cls(*args, **kwargs)
                    print('Function {} works: '.format(value.__name__, time() - current_time))

            return result
        return wrapper
    return inner_decorator


def time_of_work(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        current_time = time()
        result = function(*args, **kwargs)
        print('Function {} works: '.format(function.__name__, time() - current_time))
        return result
    return wrapper

@time_methods('inspect', 'finalize')
class Spam:
    def __init__(self, s):
        self.s = s

    @time_of_work
    def inspect(self):
        sleep(self.s)

    @time_of_work
    def foo(self):
        return self.s


a = Spam(2)
a.inspect()  # должно вывести сообщение о времени работы
a.foo()  # ничего не выводить
