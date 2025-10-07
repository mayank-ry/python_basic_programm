import os
os.system("cls")
def to_Faranheit(c):
    f = ((9/5)*c)+32
    return f

def take_Celcius():
    c = int(input("Enter Celcius To Convert It Into Faranheit : "))
    print(to_Faranheit(c))

take_Celcius()