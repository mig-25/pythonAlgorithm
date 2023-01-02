airforce = {}

aeroplane = {}

def educations():
    airforcelName = input("Ange flygvapnets namn: ")
    
    active = True
    while active:

        aeroplaneName = input("Ange flyplanets namn: ")
        # credits = int(input(f"Hur många poäng har kursen {courseName}: "))
        missiles = int(input(f"Antal missiler {aeroplaneName}: "))
        # courses[credits] = credits
        aeroplane[aeroplaneName] = missiles
        

        repeat = input("Vill du lägga till en ny flygplan? (j/n) ")
        if repeat == 'n':
            active = False

    airforce.update(aeroplane)
    
    with open("airforce.txt", "w") as f:
        f.write("Flygvapen: %s \t" % airforcelName)
        f.write("Antal missiler: %s \n" % sum(aeroplane.values()))
        
        for key, value in airforce.items():
            f.write("%s: %s\n" % (key, value))
            
    f = open("airforce.txt", "r")
    print(f.read())

educations()
