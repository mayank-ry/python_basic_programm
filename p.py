import os
os.system("cls")
"""
wap to create a dictionary of student which contains
name , branch , year , percentage ,age , A dict contains 10 students record , need to perform:
1) display name and branch those percent >75
2) age 18-23
3) name of topper student
4) older student ka details
"""
record = {
    "s1" : {"Name":"Mayank","Branch":"DS","Percent":78,"Age":18},
    "s2" : {"Name":"Aman","Branch":"DS","Percent":84,"Age":19},
    "s3" : {"Name":"sumit","Branch":"DS","Percent":55,"Age":23},
    "s4" : {"Name":"shresth","Branch":"DS","Percent":74,"Age":24},
    "s5" : {"Name":"raunak","Branch":"DS","Percent":51,"Age":22},
    "s6" : {"Name":"jaadav","Branch":"DS","Percent":55,"Age":23},
    "s7" : {"Name":"cutiee","Branch":"DS","Percent":94,"Age":27},
    "s8" : {"Name":"meow","Branch":"DS","Percent":21,"Age":30}
}
agyy = [18,19,20,21,22,23]
for key,value in record.items():
    print(f"Detail Of {value['Name']} : ",key,value)
print("--------- Above 75 Student --------- ")
for key,value in record.items():
    if value['Percent']>75:
        print(key,value)
print("--------- Age 18-23 Student --------- ")
older = 0
for values in record.values():
    if values['Age'] in agyy:
        print(f"{values['Name']} : {values['Age']}")
    if values['Age']>older:
        older = values['Age']
print(f"Older Student : {values['Name']} , Age : {older}")





