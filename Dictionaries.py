#Changing several elements in the Array-list [FromIndex:QuantityOfElements]:
d={	'Key1':[1,2,3],
	'Key2':True,
	'Key3':5,
	4:False
	}
print(d)
print(d['Key2'])
print(d[4])
d[4]=True
print(d[4])
d[4]="Hello"
print(d[4])