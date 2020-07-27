

class student():
    def __init__(self,x,y):
        print("I am a special method")
        print("x value",x)
        print("y value",y)

    def studentreg(self,Name,mob,sub,city):
        print("Student name is",Name)
        print("Student subject is",sub)
        print("student city is",city)
        print("student mob is", mob)

    @classmethod
    def studentadmin(cls,name):
        print("student name is",name)
    @staticmethod
    def studenttrip(place):
        print("stuents are travelling to",place)

c=student(20,34)
c.studentreg("leka","8870241399","Python","Tirunelveli")
c.studentreg("Sahana","8870241399","Python","canada")
c.studentadmin("sarath")
c.studenttrip("canada")

student(23,33).studenttrip("ooty")
student(22,22).studentreg("kalai",123131,"english","aus")