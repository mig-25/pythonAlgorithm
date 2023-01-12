""" Skapa två dictionaries som heter education och courses. 
Via en input ska ni spara skolansnamn och utbildningsnamn och namnet på studenten. 

Reptera SÅ LÄNGE ni vill kunna lägga till kursID och kursNamn, antal poäng för kursen och betyg
via en input, gör sedan följande:
1. lägg till dessa input läggas till i dictionary för course (alltså för en enskild kurs)

2. När ni lagt till ovan värden i dictionary för course, lägg då samtliga enskilda
kurser i dictionary för courses (alltså för en dictionariy för alla kurser)

3. Om ni inte längre vill repetera och lägga till fler kurs i kurser avsluta loopen

4a. lägg till courses i dictionary för education
4b. lägg till skolansnamn i dictionary för education
4c. lägg till utbildningensnamn i dictionary för education
4d. lägg till studentensnamn i dictionary för education

5. Skapa en textfil som heter education.txt

6. Om det finns någon kurs som har betyget IG, så ska rubriken för filen vara
Utbildningsbevis, annars om det är minst G så ska det stå Examensbevis som rubrik

7. Textfilen ska innehålla följande när hela programmet har kört klart, dvs ni måste
i resten av koden koda för följande:

Utfärdat: Utbildningsbevis	för studenten: kalle anka 
Skola: xenter 	Utbildning: itsak22 	Total antal poäng: 85 
kurs id: itsaksql
namn: sql, 35 poäng, betyg: IG
kurs id: itsakpyt
namn: python, 30 poäng, betyg: G
kurs id: itsakagl
namn: agile, 20 poäng, betyg: VG

"""

def educations():
    # initialize an empty dictionary to store courses
    courses = {}
    # initialize an empty dictionary to store education information
    education = {}
    
    student = {}

    # prompt user for school name and store input in the school_name variable
    school_name = input("Ange skolan: ")
    # prompt user for education name and store input in the education_name variable
    education_name = input("Ange utbildningen: ")
    student_name = input("Ange students namn: ")

    # set active flag to True to enter loop
    active = True
    while active:
        # prompt user for course name and store input in the course_id variable
        course_id = input("Ange kursens id: ")
        # prompt user for course name and store input in the course_name variable
        course_name = input("Ange kursens namn: ")
        # prompt user for credits and store input in the credits variable as an integer
        credits = int(input(f"Ange antal poäng för kursen {course_name}: "))
        print("Välj från följande betyg: VG\tG\tIG")
        # prompt user for score for the course and store input in the score variable
        score = input(f"Ange betyget för kursen {course_name}: ")

        # create a dictionary for the course
        course = {
            'id': course_id,  # store course name in the dictionary
            'name': course_name,  # store course name in the dictionary
            'credits': credits,  # store credits in the dictionary
            'score': score  # store score in the dictionary
        }
        # add the course dictionary to the courses dictionary
        courses[course_id] = course

        # prompt user to see if they want to add another course
        repeat = input("Vill du lägga till fler kurser? (j/n) ").lower()
        # if user does not want to add another course, set active flag to False to exit loop
        if repeat == 'n':
            active = False

    # add courses, school_name, and education_name to education dictionary
    education['courses'] = courses
    education['school_name'] = school_name
    education['education_name'] = education_name
    education['student_name'] = student_name

    # open a file in write mode to store education information
    with open("education.txt", "w") as f:

        # check if any courses have a score of "IG"
        if any(course['score'] == "IG" for course in courses.values()):
            # if any courses have a score of "IG", set status to "Certificate of Education"
            status = "Utbildningsbevis"
        else:
            # if no courses have a score of "IG", set status to "Degree Certificate"
            status = "Examensbevis"

        # write the status to the file
        f.write("Utfärdat: %s\t" % status)
        f.write("för studenten: %s \n" % student_name)
        # write the school name and education name to the file
        f.write("Skola: %s \t" % school_name)
        f.write("Utbildning: %s \t" % education_name)
        # write the total credits to the file
        f.write("Total antal poäng: %s \n" % sum(course['credits'] for course in courses.values()))

        # write the course information to the file
        for course in courses.values():
            f.write("kurs id: %s\nnamn: %s, %s poäng, betyg: %s\n" % (course['id'], course['name'], course['credits'], course['score']))

        # open the file in read mode
    f = open("education.txt", "r")
    # print the contents of the file
    print(f.read())
    
    #loop through education dictionary
    for key, value in education.items():
        print(f"{key} = {value}")


# call the educations function
educations()
