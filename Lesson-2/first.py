#Написать функцию, которая печатает квадраты всех нечетных чисел в произвольном интервале [0, Х]. А так же количество таких чисел.


def first(x):
    count = 0
    if x % 2 == 1:
        for i in range(1, x + 1, 2):
            print(i**2)
            count += 1
    else:
        for i in range(1, x, 2):
            print(i**2)
            count += 1


n = int(input())
first(n)


