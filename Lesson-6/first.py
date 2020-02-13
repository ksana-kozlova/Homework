#Напишите итератор EvenIterator, который позволяет получить из списка все элементы,
#стоящие на чётных индексах.

class EvenIterator(object):
    def __init__(self, lst):
        self.lst = lst
        self.counter = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.counter += 2
        if self.counter < len(self.lst) and self.counter % 2 == 1:
            return self.lst[self.counter]
        raise StopIteration


my_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in EvenIterator(my_lst):
    print(i)
