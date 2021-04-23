from vessels.submarine import Submarine
from weapons.torpedo import Torpedo
from powerplants.markvreactor import MarkVReactor


def main():
    ''' mark48 = Torpedo()
    mark48.aim_weapon()
    mark48.fire_weapon()

    A2W = MarkVReactor()
    A2W.ignite()
    A2W.shutDown() '''

    SeaWolf = Submarine(Torpedo(), MarkVReactor())
    SeaWolf.ignite()
    SeaWolf.aim_weapon()
    SeaWolf.fire_weapon()
    SeaWolf.shutdown()


if __name__ == "__main__":
    main()
