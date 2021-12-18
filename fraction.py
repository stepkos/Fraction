from functions import *


class Fraction:
    def __init__(self):
        self.__num = 1
        self.__den = 1
        # self.num = num  # numerator
        # self.den = den  # denominator

    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, num):
        self.__num = num

    @property
    def den(self):
        return self.__den

    @den.setter
    def den(self, den):
        self.__den = den

    def __str__(self):
        return str(self.num) + "/" + str(self.den)
