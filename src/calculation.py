from abc import ABC, abstractmethod
from math import pow
from exceptions import *

class Calculation(ABC):
    def __init__(self ,operand1: str, operand2: str):
        try:
            self._operand1 = float(operand1)
        except Exception as e:
            raise IncorrectSyntax(f" invalid syntax, {operand1} isn't a number")

        if operand2 is not None:
            try:
                self._operand2 = float(operand2)
            except Exception as e:
                raise IncorrectSyntax(f" invalid syntax, {operand1} isn't a number")

    @abstractmethod
    def result(self) -> float:
        ...

class Sub(Calculation):

    def result(self) -> float:
        return float(self._operand1)-self._operand2

class Add(Calculation):

    def result(self) -> float:
        return self._operand1 + self._operand2

class Mul(Calculation):

    def result(self) -> float:
        return self._operand1 * self._operand2

class Div(Calculation):
    def result(self) -> float:
        if self._operand2 == 0:
            raise DivisionByZero()
        else:
            return self._operand1 / self._operand2

class Pow(Calculation):
    def result(self) -> float:
        if self._operand1 < 0 and int(self._operand2) != self._operand2:
            raise RootToNegative()
        else:
            return pow(self._operand1, self._operand2)

class Avg(Calculation):
    def result(self) -> float:
        return (self._operand1 + self._operand2)/2

class Max(Calculation):
    def result(self) -> float:
        if self._operand1 > self._operand2:
            return self._operand1
        return self._operand2

class Min(Calculation):
    def result(self) -> float:
        if self._operand1 < self._operand2:
            return self._operand1
        return self._operand2

class Modolo(Calculation):
    def result(self) -> float:
        if self._operand2 == 0:
            raise DivisionByZero()
        else:
            return self._operand1 % self._operand2

class Negative(Calculation):

    def result(self) -> float:
        return -1*self._operand1

class Factorial(Calculation):

    def result(self) -> float:
        if self._operand1 < 0:
            raise NegativeInFactorial()
        if int(self._operand1) != self._operand1:
            raise FloatInFactorial()
        if self._operand1 > 170:
            raise OverflowError("the equation result is to big to calculate")

        else:
            x=1
            for i in range(2,int(self._operand1)+1):
                x*=i
            return x

class SumNum(Calculation):

    def result(self) -> float:
        if self._operand1 < 0:
            raise NegativeInSum()

        if 'e' in str(self._operand1):
            raise SumOfDigitsEError()

        sum_num=0

        for x in str(self._operand1):
            if x.isdigit():
                sum_num+=int(x)

        return sum_num


Operation={
    '-':Sub, '+':Add, '*':Mul, '/':Div,';':Negative, '^':Pow, '@': Avg, '$': Max, '&':Min,'%': Modolo,
    '~':Negative, '!':Factorial, '#':SumNum
}
