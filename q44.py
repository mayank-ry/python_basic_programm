'''import os
os.system("cls")

class calculator:
    
    def __init__(self,n):
        
     self.n=n
    def sqr(self):
          print(f"Square Of {self.n} is {self.n**2}")
    def cub(self):
           print(f"Cube Of {self.n} is {self.n**3} ")
    def sqrt(self):
           print(f"Sqrt Of {self.n} is {self.n**0.5} ")

n = int(input("Enter Integer To Do Operations : "))

calc = calculator(n)

user = input("Enter Choice For Operations (S)qr , (C)ube , or (R)oot : ").upper()

if(user=="S"):
    calc.sqr()
elif(user=="C"):
    calc.cub()
elif(user=="R"):
    calc.sqrt()
else:
 print("Invalid Choice , Try Again!")'''

import os
os.system("cls")

class calculator:
    def __init__(self,n):
        self.n=n
    def sqr(self):
        print(f"Square Of {self.n} is {self.n**2}")
    def cube(self):
        print(f"Cube Of {self.n} is {self.n**3}")
    def sqrt(self):
        print(f"Sqroot Of {self.n} is {self.n**0.5}")

n = int(input("Enter Number For Operation : "))
calc = calculator(n)
user = input("Select : (S)qr , (C)ube , Or (R)oot : ").upper()
if user=="S":
    calc.sqr()
elif user=="C":
    calc.cube()
elif user=="R":
    calc.sqrt()
else:
    print("Invalid Choice , Try Again..!!")