# OOP in Python

class Dog():
    # Constructor, instantiate the object
    # In this case, always pass in name and create dog object with a name
    def __init__(self, name, age):
        # Object attribut
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def setAge(self, age):
        self.age = age

    def bark(self):
        print('vovv vovv')

    def addOne(self, x):
        return x+1


d1 = Dog('Raja', 13)
d1.setAge(14)
print(f'The dogs name is: {d1.name} and age is: {d1.age}')
d1.bark()
print(d1.addOne(5))

d2 = Dog('Bagheera', 3)
print(f'The dogs name is: {d2.name} and age is: {d2.age}')
