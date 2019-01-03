"""Create an array list that had one integer number, one double quotation string, one Boolean, another 
array inside with at least 5 elements of your choice on it, a float number, and a single quotation string; the order 
could vary as however you like it, but all elements should be present.
The array name will be “arrayList1”. You should print it.""" 
arrayList1 = [45,"Magic", True,["Volibear",'Rengar',4,'Milo',"Kratos"],1.2,'LoL']
print('arrayList1: ',arrayList1)
#By creating a arrayList3 variable, you will fill it with the same information on the original arrayList1
arrayList3=arrayList1[0:6]
"""Afterwards, you need to change the index 3 of that array, into a number 10, and re-printing the array with the new 
data on the index 3.""" 
arrayList1[2] = 10
print('arrayList1 modify: ',arrayList1)
"""You will make some “slicing” beginning from the second index and copying 4 elements on the array arrayList1, by doing
 it on the arrayList2 variable. Then print both lists.""" 
arrayList2=arrayList1[1:4]
print('arrayList1: ',arrayList1)
print('arrayList2: ',arrayList2)
#Print arrayList3
print('arrayList3: ',arrayList3)
"""With an arrayList4 variable, you will fill it from arrayList3 variable; by copying the information on it from the first 
index, zero, but skipping every two elements."""
arrayList4=arrayList3[0:6:2]
print('arrayList4: ',arrayList4)