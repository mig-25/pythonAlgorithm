from abc import ABC, abstractmethod


class Vessel(ABC):
    def __init__(self, weapon, powerplant):
        self.weapon = weapon
        self.powerplant = powerplant
        print("Vessel object created...")

    @abstractmethod
    def ignite(self):
        pass

    @abstractmethod
    def shutdown(self):
        pass

    @abstractmethod
    def aim_weapon(self):
        pass

    @abstractmethod
    def fire_weapon(self):
        pass
