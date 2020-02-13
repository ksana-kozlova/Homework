#Написать функцию-генератор chain, которая последовательно итерирует переданные объекты
# (произвольное количество)
def chain(*iter_obgects):
    for obg in iter_obgects:
        for x in obg:
            yield x

for i in chain(['one', 'two', 'three'], (1, 2, 3), "456"):
    print(i)