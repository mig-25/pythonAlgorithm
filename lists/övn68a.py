
def ssnCheckGender():

    ssn = str(input("Mata in ditt personr, tio siffror : "))

    if int(ssn[8]) % 2 == 0:
        print(f"Personnr med nr {ssn} är en kvinna")
    else:
        print(f"Personnr med nr {ssn} är en man")


ssnCheckGender()
