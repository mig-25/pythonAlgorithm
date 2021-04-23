# Beräkna antal minuter och sekunder efer ha anget antal timmar

import math


def convertHtoM(hours):
    return math.floor(hours*60)


def convertHtoS(hours):
    return math.floor(hours*60*60)


print(
    f"Answer: {2} hours is {convertHtoM(2)} minutes and {convertHtoS(2)} seconds")
