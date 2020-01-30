#Написать функцию вычисления факториала числа


def third(n):
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    return factorial


n = int(input())
print(third(n))
