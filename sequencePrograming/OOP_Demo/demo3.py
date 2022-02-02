# OOP med arv i Python

""" class Cat():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print('Meow')


class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print('vovv vovv')
 """


class Pet():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f'Jag heter {self.name}, och är {self.age} år gammal')

    def speak(self):
        print('Jag kallas också för Gandalf Grå \n')


class Cat(Pet):
    # implement own attribut to constructor,
    # but with super take in all attributes from parent
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print('Jag säger Meow \n')

    # #Child class executes its own implementation of the the parent class method
    def show(self):
        print(
            f'Jag heter {self.name}, och är {self.age} gammal, och jag har färgen {self.color}')


class Dog(Pet):

    def speak(self):
        print('Jag säger Vovv Vovv \n')


p1 = Pet('Gandalf', 500)
p1.show()
p1.speak()

c1 = Cat('Furry', 12, 'ginger')
c1.show()
c1.speak()

d1 = Dog('Raja', 13)
d1.show()
d1.speak()
