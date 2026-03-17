t1 = (1,2,"tuple",4)
t2 = (5,6,7)
x = t2[t1[1]]
print("X is :",x)
t3 = t1 + t2
print("T3 : ",t3)
t4 = (t1,t2)
print("T4 : ",t4)
t5 = (list(t1),list(t2))
print("T5 : ",t5)
