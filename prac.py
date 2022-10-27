


from unicodedata import name


class Student:
        
    def __init__(self,name,course,accessno):
        self.name=name
        self.course=course
        self.accessno=accessno
        print("hey i have come to life")
            
    #define a function

    def eat(self):
        print("am eating")
    def sleep(self):
        print("am sleeping")  
    def drink(self):
        print("am drinking")  
    def __str__(self):
           return f"hey this is {self.name} and my course is {self.course} and my accessno is {self.acessno}"     
jim =Student("jim","bsit","a90012")
print(jim.accessno)
jimy =Student("jim","bsit","a90012")
print(jimy.accessno)

print(jim==jimy)

print(jim.eat)
print(jimy.drink)

