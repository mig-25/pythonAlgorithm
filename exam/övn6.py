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


# call the educations function
educations()
