class Employee:
    def __init__(self,idEmp,firstName,lastName,salary):
        self.__idEmp = idEmp
        self.__firstName = firstName
        self.__lastName = lastName
        self.__salary = salary
    
    def getID(self):
        return self.__idEmp
    
    def getFirstName(self):
        return self.__firstName
    
    def getLastName(self):
        return self.__lastName
    
    def getName(self):
        return self.__firstName + " " + self.__lastName
    
    def getSalary(self):
        return self.__salary
    
    def setSalary(self,salary):
        self.__salary = salary
        
    def getAnnualSalary(self):
        return self.__salary * 12
    
    def raiseSalary(self,percent):
        self.__salary += self.__salary * (percent/100)
        return self.__salary
    
    def __str__(self):
        return self.getName() + " " + str(self.getSalary())
        

class Manager(Employee):
    def __init__(self,idEmp,firstName,lastName,salary,bonus):
        super().__init__(idEmp,firstName,lastName,salary)
        self.__bonus = bonus
        
    def setBranch(self, branch):
        self.__branch = branch
    
    def getBranch(self, branch):
        return self.__branch
    
    def getBonus(self, bonus):
        return self.__bonus
    
    def setBonus(self, bonus):
        self.__bonus = bonus
        
    def getAnnualSalary(self):
        return super().getSalary() * 12 + self.__bonus
        

m1 = Manager(1234,"Guntur","Budi",5000,9000)
print(m1.getName())
print(m1.getAnnualSalary())

# e1 = Employee(1234,"Guntur","Budi",5000)
# print(e1.getSalary())
# print(e1.getAnnualSalary())
# print(e1.raiseSalary(50))
# print(e1.getAnnualSalary())
# print(e1)