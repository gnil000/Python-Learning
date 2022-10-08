import math
# Разработать
# класс
# «Деньги».
# представлено двумя полями: рубли и копейки. Дробная часть (копейки) при
# выводе на экран должна быть отделена от целой части запятой. Реализовать
# сложение, вычитание, деление сумм, деление суммы на дробное число,
# умножение на дробное число и операции сравнения.


class Money():
    rub = 0
    cop = 0

    def __init__(self, rub, cop) -> None:
        self.rub = rub
        self.cop = cop

    def set(self, rub, cop):
        self.rub = rub
        self.cop = cop

    def get(self):
        return self.rub, self.cop

    def printMoney(self):
        print(str(self.rub) + ',' + str(self.cop))

    def sumMoney(self, x):  # сумма
        first = self.rub
        first += self.cop/100
        second = x.rub
        second += x.cop/100
        first += second
        self.rub = math.floor(first)
        self.cop = int((first*100) % 100)
        return self

    def subMoney(self, x):  # разность
        first = self.rub
        first += self.cop/100
        second = x.rub
        second += x.cop/100
        first -= second
        first = abs(first)
        self.rub = math.floor(first)
        self.cop = int((first*100) % 100)
        return self

    def divMoney(self, x):  # деление
        first = self.rub
        first += self.cop/100
        first /= x
        self.rub = math.floor(first)
        self.cop = int((first*100) % 100)
        return self

    def mulMoney(self, x):  # умножение
        first = self.rub
        first += self.cop/100
        first *= x
        self.rub = math.floor(first)
        self.cop = int((first*100) % 100)
        return self

    def comparMoney(self, x):  # сравнение
        first = self.rub
        first += self.cop/100
        second = x.rub
        second += x.cop/100
        if (first > second):
            return self
        else:
            return x


mon = Money(5, 35)
mon2 = Money(6, 70)
mon.mulMoney(2.5).printMoney()
