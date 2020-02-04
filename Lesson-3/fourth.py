# На вход функции передается строка с xml документом (тэги без аттрибутов, корневой элемент только один).
# Нужно выполнить следующее преобразование и вывести максимальную вложенность.

import xmltodict


def string_to_xml(string: str):
    dct = dict(xmltodict.parse(string))

    def print_xml(dictionary, level):
        tab = '    '
        for x in dictionary:
            if dictionary[x] is None:
                print(tab * level, "{'name': ", x, "'children': [] }")
            else:
                print(tab * level, '{')
                print(tab * (level + 1), "'name': ", x)
                print(tab * (level + 1), "'children': [")
                print_xml(dictionary[x], level + 1)
                print(tab * (level + 1), ']')
                print(tab * level, '}')
        level += 1
        return level + 1

    print(print_xml(dct, 0))


xml_string = '<root><element1 /><element2 /><element3><element4 /></element3></root>'
string_to_xml(xml_string)