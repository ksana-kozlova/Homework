#Есть два списка разной длины, в одном ключи, в другом значения. Составить словарь.
# Для ключей, для которых нет значений использовать None в качестве значения.
# Значения, для которых нет ключей игнорировать.
keys = ['one', 'two', 'tree', 'four', 'fife']
values = [1, 2, 3, 4]
dict = {keys[i]: (values[i] if i < len(values) else None) for i in range(len(keys)) }
print(dict)