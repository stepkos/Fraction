class Fraction:
    gcd = staticmethod(lambda a, b: Fraction.gcd(b, a % b) if b else a)
    lcm = staticmethod(lambda a, b: a * b / Fraction.gcd(a, b))

    def __init__(self, num=1, den=1):
        self.num = num  # numerator
        self.den = den  # denominator

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

    def __str__(self) -> str:
        return str(self.num) + "/" + str(self.den)
