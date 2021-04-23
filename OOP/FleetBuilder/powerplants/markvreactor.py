from powerplants.powerplant import PowerPlant


class MarkVReactor(PowerPlant):
    def __init__(self):
        super(MarkVReactor, self).__init__()
        print("MarkV Reactor object created...")

    def ignite(self):
        print("Fission critical. Reactor powered up and ready to answer all bells")

    def shutdown(self):
        print("Reactor shutdown, cold and dark")
