# Abstract describes a concept of structure,
# Abstract classes can not be instansiated as objects

# Abstract class contain one or more abstract methods
# Abstract methods has a declartion but no implementation,
# the abstract method implementaion is done by child classes,
# but if a abstract exists they MUST be implemented by the child class

# Import abstract abc (abstract base class)
from abc import ABC, abstractmethod

# Abstract class


class Vehicle(ABC):
    # abstract method, no implemention, must be implemented by child class
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    # Implemention of abstract class methods
    def go(self):
        print("You drive the car")

    def stop(self):
        print("This car is stopped")


class Motorcycle(Vehicle):

    def go(self):
        print("You ride the motorcycle")

    def stop(self):
        print("This motorcycle is stopped")


#vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()

# vehicle.go()
car.go()
motorcycle.go()

# vehicle.stop()
car.stop()
motorcycle.stop()
