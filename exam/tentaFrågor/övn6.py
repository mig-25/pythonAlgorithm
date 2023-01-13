""" Skapa tre dictionaries som heter education, course och courses. 
Via en input ska ni spara skolansnamn och utbildningsnamn och namnet på studenten. 

Lägg till värden för course:
Reptera SÅ LÄNGE ni vill kunna lägga till kursID och kursNamn, antal poäng för kursen och betyg
via en input, gör sedan följande:
1. lägg till dessa input till i dictionary för course (alltså för en enskild kurs)

2. När ni lagt till ovan värden i dictionary för course, lägg då samtliga enskilda
kurser i dictionary för courses (alltså för en dictionariy för alla kurser)

3. Om ni inte längre vill repetera och lägga till fler kurs i kurser, så uppdatera alla
dictionaries

Uppdatera alla dictionaries:
4a. lägg till courses i dictionary för education
4b. lägg till skolansnamn i dictionary för education
4c. lägg till utbildningensnamn i dictionary för education
4d. lägg till studentensnamn i dictionary för education

5. Skapa en textfil via din kod som heter education.txt, om filen inte finns sen innan
så ska filen skapas, finns den sen innan ska innehållet skrivas över med er inmatning.

6. Om det finns någon kurs som har betyget IG, så ska rubriken för filen vara
Utbildningsbevis, annars om det är minst G så ska det stå Examensbevis som rubrik

7. Textfilen ska innehålla följande när hela programmet har kört klart, dvs ni måste
i resten av programmet koda för följande:
OBS! Print och textfilen ska ha följande formatet som nedan.
Exempel utskrift när betyget för en enskild kurs har vart IG

Utfärdat: Utbildningsbevis	för studenten: kalle anka 
Skola: xenter 	Utbildning: itsak22 	Total antal poäng: 85 
kurs id: itsaksql
namn: sql, 35 poäng, betyg: IG
kurs id: itsakpyt
namn: python, 30 poäng, betyg: G
kurs id: itsakagl
namn: agile, 20 poäng, betyg: VG

"""

""" lägg till följande kod i ert program om ni vill kontrollera att ni har rätt
herarki, dvs education har courses som har course.

#loop through education dictionary
    for key, value in education.items():
        print(f"{key} = {value}")"""