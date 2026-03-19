'''To Hide Original Detail and reconvert it through a patter'''
str1 = input("Enter A String : ")
str2 = input("Enter Another String : ")
print(sorted(str1))
print(sorted(str2))
if(sorted(str1)==sorted(str2)):
    print("These Are Anagrams")
else:
    print("These Are Not Anagrams")
    