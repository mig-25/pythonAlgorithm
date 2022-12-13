""" Avgör med personnr om det är en man eller kvinna, med formatet YYMMDDNNNN.
Om nästsista nr är jämnt delbart så är det en kvinna, annars en man.
Printa ut Man eller Kvinna.
Den nästsista nr är på indexplats 8.
Exempel:
Your input nr was: 6601255056
Man
Your input nr was: 6601253045
Woman
 """


def socialSec():

    ssn = list(int(num) for num in input(
        "Mata in ditt personnr: "))

    #print(*ssn, sep="")
    if ssn[8] % 2 == 0:
        print(f"Med personnr {ssn} är du en kvinna")
    else:
        print(f"Med personnr {ssn} är du en man")


socialSec()
