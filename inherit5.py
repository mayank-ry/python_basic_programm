class Person:
    def __init__(self, name, design):
        self.name = name
        self.design = design


class Student(Person):
    def __init__(self, name, design, roll):
        super().__init__(name, design)
        self.roll = roll
        self.complete = False

    def Assign(self):
        a = input("Enter Status (T/F): ").upper()
        if a == "T":
            self.complete = True


class Teacher(Person):
    def __init__(self, name, design, id):
        super().__init__(name, design)
        self.id = id
        self.checked = False

    def Check(self):
        a = input("Assignment Checked (Y/N): ").upper()
        if a == "Y":
            self.checked = True


class Assistant(Student, Teacher):
    def __init__(self, name, design, id, roll):
        Person.__init__(self, name, design)   # direct call (easy)
        self.id = id
        self.roll = roll

    def meow(self):
        print(f"{self.name} is {self.design}")

m = Assistant("Mayank", "Assistant", 101, 8147)
m.Assign()
m.Check()
m.meow()


    
