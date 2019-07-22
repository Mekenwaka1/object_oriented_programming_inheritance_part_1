class Person:
    def __init__(self, name):
        self.name = name
    
    def greeting(self):
        return "Hi, my name is {}".format(self.name)

class Student(Person):

    def learn(self):
        return "I get it!"

class Instructor(Person):

    def teach(self):
        return "An object is an instance of a class"

nadia = Person('Nadia')
print(Person.greeting(nadia))
chris = Person('Chris')
print(Person.greeting(chris))
print(Instructor.teach(nadia))
print(Student.learn(chris))