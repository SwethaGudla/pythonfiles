##class Student:
##    School="Ojas"
##    
##    def __init__(self, n="", m=0):
##        self.name=n
##        self.marks=m
##
##    def display(self):
##        print("HI", self.name)
##        print("Your marks",self.marks)
##
##
##    def calculate(self):
##        if(self.marks>=600):
##            print("you got first")
##        elif(self.marks>=500):
##            print("you got second")
##        elif(self.marks>=350):
##            print("you got third")
##        else:
##            print("You are Faild")
##n = int(input("Enter How many students: "))
##
##i = 0
##while (i<n):
##    name = input("Enter Name: ")
##    marks = int(input("Enter Marks: "))
##
##    s = Student(name, marks)
##    s.display()
##    s.calculate()
##    i+=1
##    print("---------------")
    
#################################################################


class Bird:
    wings = 2
    
    @classmethod
    def fly(cls,name):
        #cls.wings=3 # we can modify
        print(f'{name} flies with {cls.wings} wings')


    
Bird.fly('parrot')





























    
            
        
