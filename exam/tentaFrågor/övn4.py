''' Skapa en Dictionary för en kundvagn som ni döper till shoppingCart
Skapa en funktion som heter cart, 
i funktinen måste ni skapa följande variabeler, 
active med värdet True
counter som är satt till 0

Så länge variabeln active är sann:
    ta emot input från användaren för variabeln product
    ta emot inpout från användaren för variabeln cost
    lägg till nyckel och värde som ni har fått från input till shoppingCart
    Glöm inte att så länge active är sann också plussa på variabeln counter med 1
    
    Efter har fått in product och cost med input,
    ta emot input från användaren om dem vill lägga till fler produkter, 
    om svaret är ja, upprepa ovanstående steg, om svaret är nej,
    så sätts värdet på variabeln active till false.
    
Gå i så fall ur din loop och printa ut hur många produkter finns i kundvagnen,
loopa genom din kundvagn och med metoden items() för Dictionary, printa ut samtliga
varor och deras priser.

Använd variabeln cost som du använde som värde i din kundvagn och 
använd dig av metoden values() i din kundvagn, för att tilldela värdet i den till
variabeln cost som du skapade innan.

Använd dig av metoden sum mot din variabel cost(), tilldela sedan resultatet i en variabel
som heter Total

Printa sedan ut totalkostnaden för hela kundvagnen från varibeln Total.

Exempel:
    Lägg till varor och ange pris


-----------Varor---------------
Ange vara: tandborste
vad kostar varan: 24
Vill du lägga till fler varor? (j/n) j
Ange vara: tandkräm
vad kostar varan: 12
Vill du lägga till fler varor? (j/n) j
Ange vara: schampo
vad kostar varan: 45
Vill du lägga till fler varor? (j/n) j
Ange vara: after shave
vad kostar varan: 560
Vill du lägga till fler varor? (j/n) n


Din kundvagn innehåller 4 varor:
---------------------------------
Varan: tandborste, pris: 24 kr
Varan: tandkräm, pris: 12 kr
Varan: schampo, pris: 45 kr
Varan: after shave, pris: 560 kr
--------- Summan: 641 kr --------
     '''