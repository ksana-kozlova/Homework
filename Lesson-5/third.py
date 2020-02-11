class Observable():

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __str__(self):
        public_attr = {}
        for (key, value) in self.__dict__.items():
            if key[0] != '_':
                public_attr.update({key: value})
        dictionary = ', '.join('{}={}'.format(key, value) for (key, value) in public_attr.items())
        return '{}({})'.format(self.__class__.__name__, dictionary)

class X(Observable):
    pass

x = X(foo=1, bar=5, _bazz=12, name='Amok', props=('One', 'two'))
print(x)
print(x.foo)
print(x.name)
print(x._bazz)