#Написать функцию-генератор cycle которая бы возвращала циклический итератор.
my_obg = ['one', 'two', 'three']

def cycle(my_iter_obg):
    lst = list(my_iter_obg)
    i = 0
    while True:
        yield lst[i]
        i = i + 1
        if i >= len(lst):
            i = 0

for i in cycle(my_obg):
    print(i)