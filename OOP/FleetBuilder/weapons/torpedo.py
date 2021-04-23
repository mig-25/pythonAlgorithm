from weapons.weapon import Weapon


class Torpedo(Weapon):
    def __init__(self):
        super(Torpedo, self).__init__()
        print("Torpedo object created...")

    def aim_weapon(self):
        print("Torpedo is armed and ready to fire...Target aquired!!!")

    def fire_weapon(self):
        print("Torpedo away...swoosh...zzzz...KABBOM...Target destroyed!!!")
