# Omvandla 2 timmar till minuter och sekunder, använd två olika funktioner och printa svaret

import math


def convertHtoM(hours):
    return math.floor(hours*60)


def convertHtoS(hours):
    return math.floor(hours*60*60)


print(
    f"Answer: {2} hours is {convertHtoM(2)} minutes and {convertHtoS(2)} seconds")
