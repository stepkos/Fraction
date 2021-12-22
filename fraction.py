class Fraction:
    gcd = staticmethod(lambda a, b: int(Fraction.gcd(b, a % b) if b else a))
    lcm = staticmethod(lambda a, b: int(a * b / Fraction.gcd(a, b)))

    def __init__(self, num=1, den=1):
        self.num = num  # numerator
        self.den = den  # denominator
        self.gcd = lambda: Fraction.gcd(self.num, self.den)
        self.lcm = lambda: Fraction.lcm(self.num, self.den)
        self.shorten()

    @classmethod
    def hotReturn(cls, num, dec):
        return cls(num, dec)

    @classmethod
    def fromInt(cls, val):
        return cls(val)

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

    def getValues(self):
        return self.num, self.den

    @staticmethod
    def __argumentToFraction(func):
        def wrapper(self, other):
            if type(other) == type(self):
                pass
            elif type(other) == int:
                other = Fraction.fromInt(other)
            else:
                raise TypeError
            return func(self, other)

        return wrapper

    # x + y -> x.__add__(y)
    @__argumentToFraction.__get__('')
    def __add__(self, other):
        num, den = self.getValues()
        lcm = Fraction.lcm(den, other.den)
        num *= (lcm // den)
        other.num *= (lcm // other.den)
        return Fraction().hotReturn(num + other.num, lcm)


    # x - y -> x.__sub__(y)
    def __sub__(self, other):
        pass

    # x * y -> x.__mul__(y)
    @__argumentToFraction.__get__('')
    def __mul__(self, other):
        num, den = self.getValues()
        num *= other.num
        den *= other.den
        return Fraction.hotReturn(num, den)

    # x / y -> x.__truediv__(y)
    @__argumentToFraction.__get__('')
    def __truediv__(self, other):
        num, den = self.getValues()
        den *= other.num
        num *= other.den
        return Fraction.hotReturn(num, den)

    # x ** y -> x.__pow__(y)
    def __pow__(self, power: int, modulo=None):
        # modulo to implement in future
        num, den = self.getValues()
        originalNum, originalDen = num, den
        for _ in range(power - 1):
            num *= originalNum
            den *= originalDen

        return Fraction.hotReturn(num, den)

    # x < y -> x.__lt__(y)
    def __lt__(self, other):
        pass

    # x <= y -> x.__le__(y)
    def __le__(self, other):
        pass

    # x == y -> x.__eq__(y)
    def __eq__(self, other):
        pass

    # x != y -> x.__ne__(y)
    def __ne__(self, other):
        pass

    # x > y -> x.__gt__(y)
    def __gt__(self, other):
        pass

    # x >= y -> x.__ge__(y)
    def __ge__(self, other):
        pass

    def __call__(self, exp):
        if type(exp) == str:
            if len(exp) == 1:
                self.num = int(exp)
                self.den = 1
            else:
                self.num, self.den = map(int, exp.split('/'))
        elif type(exp) == int:
            self.num = exp
            self.den = 1
        else:
            raise TypeError

    def __str__(self):
        if self.den == 1:
            return str(self.num)
        return str(self.num) + '/' + str(self.den)