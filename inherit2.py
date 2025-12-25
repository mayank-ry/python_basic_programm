""". Create a class Student that stores roll no and 
name. Create class Marks that inherits Student and calculates total and percentage."""
class Student:
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll
class Marks(Student):
    def __init__(self,name,roll,eng,hindi,math):
        super().__init__(name,roll)
        self.eng = eng
        self.hindi = hindi
        self.math = math
    def total(self):
        self.totals = self.eng + self.hindi + self.math
        print("Total :", self.totals)
        return self.totals
    def per(self):
        self.total()
        self.percent = self.totals / 3
        print("Percentage :", self.percent)
        return self.percent
S1 = Marks("Mayank","E101",85,95,84)
S1.total()
S1.per()