#Написать генератор списка для получения списка всех публичных атрибутов объекта
#выражение-генератор
obg = list
my_list = [attr for attr in dir(obg) if not attr.startswith('_')]
print(my_list)

#функция-генератор
def gen_public_attr(obg):
    for attr in dir(obg):
        if not attr.startswith('_'):
            yield attr

for x in gen_public_attr(list):
    print(x)
