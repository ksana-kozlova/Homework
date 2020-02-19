# Напишите параметризованный декоратор, который считает и выводит при каждом вызове
# среднее время работы функции за n последних вызовов.
# Время выводить в миллисекундах.
from time import sleep, time
from functools import wraps


def average_time(n=2):
    def inner_decorator(function):
        count = -1
        times = []
        @wraps(function)
        def wrapper(*args, **kwargs):
            nonlocal count
            count += 1
            current_time = time()
            result = function(*args, **kwargs)
            this_time = int(round(time() - current_time) * 1000)
            times.append(this_time)
            if count >= n - 1:
                sum_of_times = sum((times[i] for i in range(len(times) - n, len(times))))
                aver_time = int(sum_of_times / n)
            else:
                sum_of_times = sum((times[i] for i in range(0, len(times))))
                aver_time = int(sum_of_times / len(times))
            print('Среднее время работы: {} мс.'.format(aver_time))

            return result
        return wrapper
    return inner_decorator


@average_time(n=2)
def foo(a):
    sleep(a)
    return a

# функция может вывести среднее время работы функции за любое введённое количество раз


foo(3)
foo(7)
foo(1)
