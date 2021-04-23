from abc import ABC, abstractmethod


class Weapon(ABC):
    def __init__(self):
        print("Weapon object created...")

    @abstractmethod
    def aim_weapon(self):
        pass

    @abstractmethod
    def fire_weapon(self):
        pass
