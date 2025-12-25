""". Create a base class Employee. Child classes:
FullTimeEmployee and PartTimeEmployee. Calculate salary differently for each"""
class Employee:
    def __init__(self,name,daySalary):
        self.name = name
        self.daySalary = daySalary
class Part(Employee):
    def __init__(self,name,daySalary):
        super().__init__(name,daySalary)
    def calc_month(self):
        monthly = self.daySalary*30
        print(f"{self.name} Earns {monthly} Per Month")
    
class Full(Employee):
    def __init__(self,name,daySalary):
        super().__init__(name,daySalary)
    def calc_month(self):
        monthly = self.daySalary*30
        print(f"{self.name} Earns {monthly} Per Month")
    
mayank = Part("Mayank",510)
mayank.calc_month()

    
