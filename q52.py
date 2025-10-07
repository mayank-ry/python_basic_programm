from datetime import date
print(date.today())
a = input("Enter Food1 Name : ")
a1 = float(input("Enter Food1 Price : "))
a2 =float(input("Enter Quantity : "))
G1 = a1*a2

b = input("Enter Food2 Name : ")
b1 = float(input("Enter Food2 Price : "))
b2 = float(input("Enter Quantity : "))
G2 = b1*b2

c = input("Enter Food3 Name : ")
c1 = float(input("Enter Food3 Price : "))
c2 = float(input("Enter Quantity : "))
G3 = c1*c2

Bill = G1+G2+G3
GST = Bill*0.05
print(GST)
Total = Bill + GST
print("Total After 5% GST : ",Total)


