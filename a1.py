#parent class

class person():
    def __init__(self,n,a):
        self.name=n # instance member/data member
        self.age=a # instance member/data member
    def intro(self):
        print(self.name)
        print(self.age)

#child class
class employee(person): #employee is child class of person
    def __init__(self,n,a,s,d):
        self.salary=s
        self.designation=d
        person.__init__(self,self.salary,self.designation) #calling parent class constructor
        super().__init__(self.salary,self.designation)
        #super().__init__(n,a)

    def employeeDetails(self):
        print(self.salary)
        print(self.designation)

o1=employee("Devanshu",31,64000,"Officer")
o1.intro()
o1.employeeDetails()