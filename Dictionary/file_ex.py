details={'Name' : "Alice",
         'Age' : 21,
         'Degree' : "Bachelor Cse",
         'University' : "Northeastern Univ"}
  
with open("myfile.txt", 'w') as f: 
    for key, value in details.items(): 
        f.write('%s:%s\n' % (key, value))
        
f = open("myfile.txt", "r")
print(f.read()) 