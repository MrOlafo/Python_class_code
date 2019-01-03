"""Create an array list in Python that had one integer number, one double quotation string, one Boolean, 
another array inside with at least 3 elements of your choice on it, a float number, and a single quotation string; 
the order could vary as however you like it, but all elements should be present. The array name will be 
“readyList1”. You should print it. """ 
readyList1 = [21,"Apartament", True,["Allan",'Adriana',2],53.35,'CONCASA']
print('readyList1: ',readyList1)
#By creating a readyList3 variable, you will fill it with the same information on the original readyList1
readyList3=readyList1[0:6]
"""Afterwards, you need to change the third index of that array, into a number 5, and re-printing the array with
 the new data on the third index.""" 
readyList1[2] = 5
print('readyList1 modify: ',readyList1)
"""- You will make some “slicing” beginning from index 1 and copying 3 elements on the array readyList1, by doing 
it on the readyList2 variable. Then print both lists""" 
readyList2=readyList1[1:4]
print('readyList1: ',readyList1)
print('readyList2: ',readyList2)
#Print readyList3
print('readyList3: ',readyList3)
"""With a readyList4 variable, you will fill it from readyList3 variable; by copying the information on it from index 0,
 but skipping every two elements."""
readyList4=readyList3[0:6:2]
print('readyList4: ',readyList4)