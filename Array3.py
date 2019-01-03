#Changing several elements in the Array-list [FromIndex:QuantityOfElements]:
l5 = [2,"Tres", True,["uno",10],6]
l5[0:2] = [4,3]
print(l5)
#Modify several elements in the Array-list with just one data [FromIndex:QuantityOfElements]:
l6 = [2,"Tres", True,["uno",10],6]
l6[0:2] = [5]
print(l6)
#Get data from an array with negative index:
l6 = [2,"Tres", True,["uno",10],6]
l7 = l6[-1]
l8 = l6[-2]
print(l7)
print(l8)