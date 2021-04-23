from abc import ABC, abstractmethod


class PowerPlant(ABC):
    def __init__(self):
        print("Powerplant object created...")

    @abstractmethod
    def ignite(self):
        pass

    @abstractmethod
    def shutdown(self):
        pass
