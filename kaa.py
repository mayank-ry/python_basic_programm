import json
import os 
os.system("cls")
x =  '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)
print(y['age'])
print(type(x))
print(type(y))