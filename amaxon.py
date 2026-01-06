import os
os.system("cls")
record = {
    "s1" : {"Name":"Watch","Cate":"Elect","Price":78,"Q":18,"Dis":15},
    "s2" : {"Name":"Clock","Cate":"Elect","Price":84,"Q":19,"Dis" : 15},
    "s3" : {"Name":"Phone","Cate":"Elect","Price":55,"Q":23,"Dis" : 15},
    "s4" : {"Name":"Laptop","Cate":"Elect","Price":74,"Q":24,"Dis": 15},
    "s5" : {"Name":"Pant","Cate":"Cloth","Price":54,"Q":22,"Dis":15},
    "s6" : {"Name":"Shirt","Cate":"Cloth","Price":55,"Q":23,"Dis":15},
    "s7" : {"Name":"Ghagra","Cate":"Cloth","Price":94,"Q":27,"Dis":15},
    "s8" : {"Name":"Copies","Cate":"Stationery","Price":21,"Q":30,"Dis":15}
}
category = {
    "Elect" : 0,
    "Cloth" : 0,
    "Stationery" : 0
}
for key,values in record.items():
        if values["Cate"]=="Elect":
            category['Elect']+=1
        elif values["Cate"]=="Cloth":
            category['Cloth']+=1
        else:
            category['Stationery']+=1
print("Number Of Cateories : ",category)
maxi = max(category.values())
print("Max Product Of Category : ",maxi)
for key,value in category.items():
     if value==maxi:
          print(f"Maximum Product = {key} : {value}")

minim = min(category.values())
print("Min Product Of Category : ",minim)
for key,value in category.items():
     if value==minim:
          print(f"Minimum Product = {key} : {value}")
