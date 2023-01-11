airforce = {}
squadron = {}
aeroplanes = {}
status = ""

def airforces():
    airforcelName = input("Ange flygvapnets namn: ")
    
    squadronName = input("Ange flygskvadronens namn: ")
    
    squadronLocality = input("Ange orten för flygskvadronens: ")
    
    # så länge du vill lägga till fler flygplan
    active = True
    while active:

        aeroplaneName = input("Ange flyplanets namn: ")
        pilotName = input("Ange pilotens namn: ")
        shotDown = int(input(f"Antal fiender som {pilotName} har skjutit ner: "))
        
        aeroplane = {
            "aeroplaneName": aeroplaneName,  # lägg till flygplanets namn
            "pilotName": pilotName, # lägg till pilotens namn
            "shotDown": shotDown  # antal nedskjutna plan
        }
        # lägg till dictionary för varje enskild flygplan till dictionary för alla flygplan
        aeroplanes[aeroplaneName] = aeroplane
        
        # vill du lägga till fler flygplan
        repeat = input("Vill du lägga till en ny flygplan? (j/n) ")
        if repeat == 'n':
            active = False

    # lägg till namnet på flygvapnet till dictionary airfoce
    airforce['airforcelName'] = airforcelName
    # lägg till namnet på skvadronen till dictionary airfoce
    squadron['squadronName'] = squadronName
    # lägg till orten för skvadronen till dictionary squadron
    squadron['squadronLocality'] = squadronLocality
    # lägg till hela dictionary för alla flygplan till dictionary squadron
    airforce['aeroplanes'] = aeroplanes
    airforce['squadronName'] = squadron
    
    # skapa en fil med namnet airforces.txt
    with open("airforces.txt", "w") as f:
        # om någon enskild flyplan i dictionary aeroplanes har skjutit ner mer än 5 fiender
        if any(aeroplane['shotDown'] > 5 for aeroplane in aeroplanes.values()):
            status = "Skvadronen har flygaress"
        else:
            status = "Skvadronen har standard piloter"
            
        f.write("Flygvapen: %s \n\n" % airforcelName) # visa flygvapenets namn
        f.write("Utfärdat: %s\n" % status) # visa rätt status som rubrik
        f.write("Flygflottilj: %s,\t" % squadronName) # visa flottiljensnamn
        f.write("Förlagd: %s,\t" % squadronLocality) # visa flottiljs ort
        # visa antal sammanlagda fi nedskjutna
        f.write("Total nedskjutna flygplan: %s\n\n" % sum(aeroplane['shotDown'] for aeroplane in aeroplanes.values()))
        f.write("-----------------Flygplan på: %s-----------------\n\n" % squadronName)
        
        # loopa genom all data för varje enskilt flygplan 
        for aeroplane in aeroplanes.values():
            f.write("Flygplanet: %s,\nNedskjutna fiender: %s,\t Pilotens namn: %s\n\n" % (aeroplane['aeroplaneName'], aeroplane['shotDown'], aeroplane['pilotName']))
            
    f = open("airforces.txt", "r")
    print(f.read())
    
    # show all data för hela flygvapnet
    for key, value in airforce.items():
        print(f"{key} = {value}")

airforces()
