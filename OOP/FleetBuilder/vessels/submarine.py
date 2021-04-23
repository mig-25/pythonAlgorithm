from vessels.vessel import Vessel


class Submarine(Vessel):
    def __init__(self, weapon, powerplant):
        super(Submarine, self).__init__(weapon, powerplant)
        print("Submarine object created...")

    def ignite(self):
        self.powerplant.ignite()

    def shutdown(self):
        self.powerplant.shutdown()

    def aim_weapon(self):
        self.weapon.aim_weapon()

    def fire_weapon(self):
        self.weapon.fire_weapon()
