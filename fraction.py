class Fraction:
    gcd = staticmethod(lambda a, b: Fraction.gcd(b, a % b) if b else a)
    lcm = staticmethod(lambda a, b: a * b / Fraction.gcd(a, b))

    def __init__(self, num=1, den=1):
        self.num = num  # numerator
        self.den = den  # denominator
        self.gcd = lambda: Fraction.gcd(self.num, self.den)
        self.lcm = lambda: Fraction.lcm(self.num, self.den)
        self.shorten()

    @classmethod
    def hotReturn(cls, num, dec):
        return cls(num, dec)

    @property
    def num(self) -> int:
        return self.__num

    @num.setter
    def num(self, num: int):
        self.__num = num

    @property
    def den(self) -> int:
        return self.__den

    @den.setter
    def den(self, den: int):
        if den == 0:
            raise ZeroDivisionError
        self.__den = den

    def shorten(self):
        div = self.gcd()
        if div > 1:
            self.__num //= div
            self.__den //= div

    def __mul__(self, other):
        num, den = self.num, self.den

        if type(other) == type(self):
            num *= other.num
            den *= other.den
        elif type(other) == int:
            num *= other
        else:
            raise TypeError

        return Fraction.hotReturn(num, den)

    def __truediv__(self, other):
        num, den = self.num, self.den

        if type(other) == type(self):
            den *= other.num
            num *= other.den
        elif type(other) == int:
            den *= other
        else:
            raise TypeError

        return Fraction.hotReturn(num, den)

    def __str__(self):
        if self.den == 1:
            return str(self.num)
        return str(self.num) + '/' + str(self.den)