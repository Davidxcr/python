
class Person():
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job
    
    def message(self):
        print("Hi my name is ", self.name, 'and i am ', self.age, ' years old, and i am a', self.job)

Femi = Person('Femi', 25, 'Student')
Femi.message()