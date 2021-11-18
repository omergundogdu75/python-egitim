# Kalıtım inheritance: Miras alma
# Person => name,lastname, age,eat(),run(),drink()
# Student(Person), Teacher(Person)

# Animal => Dog(),Cat()

class Person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        print("Person Created")
    def who_am_i(self):
        print("I am a Person p")
    def eating(self):
        print("I am a eating P")

class Student(Person):
    def __init__(self,fname,lname,number):
        Person.__init__(self,fname,lname)
        print("Student Created")
        self.number = number
    def who_am_i(self):
        print("I am a Person S")

    def sayHello(self):
        print(f"Hello I am a stundet")

class Teacher(Person):
    def __init__(self,fname,lname,branch):
        super().__init__(fname,lname)
        self.branch = branch

    def who_am_i(self):
        print(f"I am a {self.branch} Teacher")

p1 = Person("ÖMER","GND")
s1 = Student("ÖMER2","GND2",1234)
t1 = Teacher("ÖMER","GÜNDOĞDU","GND")
s1.sayHello()
print(f"{p1.fname} {p1.lname}")
print(f"{s1.fname} {s1.lname} {s1.number}")

t1.who_am_i()

