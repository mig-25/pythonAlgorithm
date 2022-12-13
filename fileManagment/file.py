def fileManagment():
    f = open("test.txt", "w")
    f.write("SAAB makes the best aeroplanes \n")
    f.close()
    
    #open and read the file after the appending
    f = open("test.txt", "r")
    print(f.read())
    
    f = open("test.txt", "a")
    f.write("SAAB Viggen rules")
    f.close()
    
    #open and read the file after the appending
    f = open("test.txt", "r")
    print(f.read())
    
fileManagment()    