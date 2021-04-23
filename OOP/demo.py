from abc import ABC, abstractmethod


class Aircraft(ABC):

    @abstractmethod
    def __init__(self, speed):
        self.__speed = speed

    @property
    @abstractmethod
    def speed(self):
        pass

    @speed.setter
    @abstractmethod
    def speed(self, value):
        pass

    @abstractmethod
    def fly(self):
        pass

    @abstractmethod
    # This abstract method must be implemented as all abstract
    # methods, but can also be overidden in the concrete class
    def land(self):
        print("All checks completed")

# Cannot instiansate a abstract class
#a1 = Aircraft()


''' class Jet(Aircraft):
    pass '''


# Abstract method be implemented in concrete class
#j1 = Jet()

class Jet(Aircraft):
    def __init__(self, speed):
        self.__speed = speed

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        self.__speed = value

    def fly(self):
        print("My jet is flying")

    def land(self):
        super().land()
        print("My jet has landed")


j1 = Jet(900)
j1.fly()
print(f"Speed is set to {j1.speed}")
j1 = Jet(950)
print(f"Speed is set to {j1.speed}")

j1.land()
