#Написать функцию, которая принимает 3 числа (a,b,c) и проверяет сколько чисел между ‘a’ и ‘b’ делятся на ‘c’


def second(a, b, c):
    count = 0
    for x in range(a + 1, b):
        if x % c == 0:
            count += 1
    return count


x, y, z = map(int, input().split())
print(second(x, y, z))
