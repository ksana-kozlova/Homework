# first

'''
def first(s=input()):
    words = s.split(' ')
    capitalized_words = []
    for word in words:
        cap_word = word[0].upper() + word[1:]
        capitalized_words.append(cap_word)
    output = ' '.join(capitalized_words)
    return output


print(first())
'''
# second
'''

def second(s=input()):
    symbols = {}
    for i in s:
        if i in symbols:
            symbols[i] += 1
        else:
            symbols[i] = 1
    return symbols


print(second())'''

# third
'''


def third(s=input()):
    if len(s) > 1:
        return s[:2] + s[-2:]
    else:
        return ""


print(third())

'''
# fourth
'''

def fourth(strings=['jhgfa', 'ada', 'ghkmbg', 'f']):

    count = 0
    for str in strings:
        if len(str) >= 2 and str[0] == str[-1]:
            count += 1
    return count


print(fourth())'''


# fifth
'''def fifth(first_set=set([1, 2]), second_set=set([2, 3]), third_set=set([2])):
    return first_set.issuperset(third_set) and second_set.issuperset(third_set)


print(fifth())'''


# sixth

'''
def sixth(n=int(input())):
    dictionary = {a: a ** 2 for a in range(1, n + 1)}
    return dictionary


print(sixth())
'''
# seventh

'''
def seventh(first_dict, second_dict):
    dictionary = first_dict.copy()
    dict.update(second_dict)
    return dictionary


print(seventh())
'''

# eighth

'''
def eighth(dictionary={a: a ** 2 for a in range(1, 7)}):
    from collections import Counter
    k = Counter(dictionary)
    high = k.most_common(3)
    return high


print(eighth())
'''
# ninth

'''
def ninth(input_list=[1, 1, 2, 3, 3, [4, 5, 6]]):
    output = []
    for x in input_list:
        if x not in output:
            output.append(x)
    return output


print(ninth())
'''
# tenth
'''

def tenth(list1=[1, 1, 2, 3, 3, [4, 5, 6]], list2=[3, 5]):
    output = []
    for x in list1:
        if x not in list2:
            output.append(x)
    return output


print(tenth())
'''