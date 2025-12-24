import os
os.system("cls")
#wap to check given identifier is valid or not
"""
special character not
start with _ and alpha yes
space not
minimum 1 character
python keywords not
"""

# import keyword
# name = input("Enter Identifier : ")
# if keyword.iskeyword(name):
#     print("Its Invalid")
# elif name[0]== ' ' or name[0] in "0123456789~`@!#$%^&*()_+=-":
#     print("Invalid")
    
# else:
#     for i in range(1,len(name)):
#         if name[i]== ' ' or name[i] in '~`!@#$%^&*()_+=-':
#             print("Invalid Name")
#             break
#         else:
#             print('valid name')
#             break

'''

minimum len 8
min 1 digit
min 1 special char
min 1 uppercase
min 1 lowercase
start with letter

'''
password = input("Enter A Password : ")
a = "@#$%&!"
for i in range(1,len(password)):
    if password[i]== ' ' or password[i] in "!@#$%&":
      pass
    else:
        print("Atleast One Character")
        break
       
if len(password)<8:
    print("Minimum 8 Char Bro")
