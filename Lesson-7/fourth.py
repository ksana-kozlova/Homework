# Написать декоратор, который будет проверять тип аргументов при вызове функции согласно аннотации функции.
# Декорирование функции без аннотации или с неполной аннотацией должно рейзить ошибку.
# В случае несовпадения переданных во время вызова функции аргументов с типами аргументов выводить сообщение.


def check_type(function):
    def wrapped(*args):
        annotations = function.__annotations__.values()
        if len(args) != len(annotations):
            raise TypeError('Need type annotation for all variables')
        for (variable, annotation) in zip(args, annotations):
            if type(variable) != annotation:
                print('The type {} of variable {} does not match '
                      'the type {} in the annotation'.format(type(variable), variable, annotation))
        return function(*args)
    return wrapped


@check_type
def foo(a: int, b: str, c: list):
    c.append(a * b)
    return c


foo(1, 'mama', [])
