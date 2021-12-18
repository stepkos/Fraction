from functions import *


class Fraction:
    def __init__(self, num=1, den=1):
        self.num = num  # numerator
        self.den = den  # denominator

    @property
    def num(self) -> int:
        return self.__num

    @num.setter
    def num(self, num: int) -> None:
        self.__num = num

    @property
    def den(self) -> int:
        return self.__den

    @den.setter
    def den(self, den: int) -> None:
        if den == 0:
            raise ZeroDivisionError
        self.__den = den

    def __str__(self) -> str:
        return str(self.num) + "/" + str(self.den)
