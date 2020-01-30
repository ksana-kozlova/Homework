#Написать свою имплементацию функции range() из Python 2.x (аналогично Python 3, только возвращает список).


def fourth(start=None, stop=None, step=1):
    list = []
    if start == None :
        return "fault"
    if stop == None:
        i = 0
        while i < start:
            list.append(i)
            i += step
        return list
    if step == 0:
        return "fault"
    i = start
    if step > 0:
        while i < stop:
            list.append(i)
            i += step
    else:
        while i > stop:
            list.append(i)
            i += step
    return list


for i in fourth(-3, 9, 1):
    print(i)







