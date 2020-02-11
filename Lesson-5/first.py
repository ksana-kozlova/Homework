from math import sqrt

class Complex(object):
    def __init__(self, re, im = 0.0):
        self.re = re
        self.im = im

    def __add__(self, other):
        return Complex(self.re + other.re, self.im + other.im)

    def __sub__(self, other):
        return Complex(self.re - other.re, self.im - other.im)

    def __mul__(self, other):
        return Complex(self.re * other.re - self.im * other.im,
                       self.re * other.im + other.re * self.im)

    def __truediv__(self, other):
        return Complex((self.re * other.re + self.im * other.im) / (other.re ** 2 + other.im ** 2),
                       (other.re * self.im - self.re * other.im) / (other.re ** 2 + other.im ** 2))

    def __abs__(self):
        return Complex(sqrt(self.re**2 + self.im**2))

    def __str__(self):
        if self.im >= 0:
            return '{:.2f}+{:.2f}i'.format(self.re, self.im)
        return '{:.2f}{:.2f}i'.format(self.re, self.im)

def mod(complex_number):
    return abs(complex_number)

if __name__ == '__main__':
    C = Complex(*list(map(int, str(input()).split())))
    D = Complex(*list(map(int, str(input()).split())))
    print(C + D)
    print(C - D)
    print(C * D)
    print(C / D)
    print(mod(C))
    print(mod(D))