from abc import ABC, abstractmethod


class Myabs(ABC):

    def __init__(self, connection):
        self.connection = connection
        print("Från den abstrakta klassen : {}".format(self.connection))

    @abstractmethod
    def fun1(self):
        pass


class D(Myabs):
    def fun1(self):
        print("calling from D: fun1")


test = D('konstruktorn från den abstrakta klassen')
test.fun1()
