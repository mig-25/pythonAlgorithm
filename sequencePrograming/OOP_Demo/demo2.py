# Grading system

class Student():
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade  # 0 - 100

    def getGrade(self):
        return self.grade


class Course():
    def __init__(self, name, maxStudents):
        self.name = name
        self.maxStudents = maxStudents
        # attribut for list of students to use with a method for adding them
        self.students = []

    # method for adding students to course
    # if array of studens is smaller then max students, add to array students
    def addStudent(self, student):
        if len(self.students) < (self.maxStudents):
            self.students.append(student)

            return True
        for student in self.students:
            print(
                f' Inskrivna: {student.name}')
        else:
            print(
                'Kan inte lägga till fler studenter')
        return False

    # method to getting average grade of all students
    def getAverageGrade(self):
        value = 0
        for student in self.students:
            value += student.getGrade()

        return value / len(self.students)


s1 = Student('Sohail', 55, 100)
s2 = Student('Kalle', 45, 34)
s3 = Student('Kajsa', 40, 98)

# Skapa ny kurs med namnet Trafikpilot med max 2 studenter
course = Course('Trafikpilot', 2)
print(f'Max antal studenter är: {course.maxStudents}')

# Lägg till två studenter
course.addStudent(s1)
course.addStudent(s2)

# print(course.students[0].name)

# när vi lägger till den tredje studenten, max antal är 2
# så blir utfallet falsk, och medel kavarstår som innan
print(course.addStudent(s3))


print(f'Medelbetyget är: {course.getAverageGrade()}')
