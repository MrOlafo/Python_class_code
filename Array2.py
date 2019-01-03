#Modifying inner array's data with the index:
l=[2,"Tres",True,["Uno",10]]
l[1]=4
l2=l[1]
print(l2)
#Slicing: Copy some informartion from an Array towards another one [begginingIdex:QuantityOfCopyElements]: 
l3=l[0:3]
l7=l[1:2]
print(l3)
#Copy some information from an Array towards another one by skipping some information [begginingIdex:QuantityOfCopyElements:AmountOfSkipsPerIndex]:
l4=l[0:3:2]
print(l4)
#Copy some information from an Array towards another one by skipping each we want [begginingIdex:QuantityOfCopyElements:AmountOfSkipsPerIndex]:
l5=l
l6=l5[0::2]
print(l5)
print(l6)