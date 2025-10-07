'''import os
os.system("cls")
a = input("Enter Anything You Want : ")
while a!="stop":
    user = input("Want To Continue (y/n) : ").lower()
    if user=="y":
        pass
        while a=="stop":
            break
        else:
         a = input("Enter Anything You Want : ")
    elif user=="n":
        print("----Programme Has Been Stopped----")
        break
    else:
        print("Enter Valid Choice")'''

import os
os.system("cls")
while True:
    a = input("Enter Anything : ").lower()
    if a=="stop":
        print("----Programm Ended Successfully----")
        break
    user = input("Want To Continue (y/n) : ").lower()
    if user=="n":
     print("----Programm Is Ended----")
     break
    elif user=="y":
     pass
    else:
       print("Enter A Valid Choice")
       break






