


from os import access
from sqlite3 import ProgrammingError
from unicodedata import name


class Person:

    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
       return f"The name is{self.name}"
person1=Person("claire",43)
the_second_person= Person("ann",67)
print(person1)

class Student(Person):
    def __init__(self,name,age,accessno,program):
        super().__init__(name,age)
        self.accessno=accessno
        self.program=program
    def start_walking(self):
        print(f"{self.name} is walking🚶‍♀️.......")

   
    def __str__(self):
     return f"The studentname{self.name} and the age is{self.age}"
student1=Student("claire",13),"a95293","bsit"
print(student1)
student1.start_walking()     