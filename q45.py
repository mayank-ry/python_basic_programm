import os
os.system("cls")
from random import randint
class train:
    Owner = "Indian Railway"
    trainNumber=454545
    fro="Indore"
    to="Bhopal"
    price=450
    seat=960
    def __init__(self,trainNumber):
        self.trainNumber=trainNumber
    def getStatus(self,trainNumber,fro,to):
        print(f"Train {trainNumber} Is Running Successfully From {fro} to {to}")
    def getFare(self,trainNumber,price):
        print(f"Ticket Fare For Train {trainNumber} Is : {price}")
    def getSeat(self,trainNumber,seat):
        print(f"Total Number Of Seats In {trainNumber} Are : {seat}")



choice = int(input("Enter Your Train Number To Get Details : "))
Info = train.trainNumber
user = input("Select Information To Print (F)are , (S)tatus, (T)seats ").upper()
if choice==Info:
 if user=="F":
    Info.getFare()
 elif user=="S":
    Info.getStatus()
 elif user=="T":
    Info.getSeat()
 else:
    print("---------Invalid Choice , Try Again!---------")