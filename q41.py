import os
os.system("cls")
def cel_to_far(c):
    f = ((9/5*c)+32)
    return f

def far_to_cel(f):
    c = (5/9*(f-32))
    return c

user = input("Enter Your Choice (C)_to_f , (F)_to_c or (E)xit : ")
if (user=="C"):
    c = float(input("Enter Temperature (C) To Convert Into Faranheit : "))
    print("Conversion Is : ",cel_to_far(c))
elif (user=="F"):
    Temp = float(input("Enter Temperature (F) To Convert Into Celcius : "))
    print("Conversion Is : ",far_to_cel(Temp))
elif(user=="E"):
    print("--------Programme Exited Successfully!--------")
else:
    print("Invalid Choice , Try Again...")
    

