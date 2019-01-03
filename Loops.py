age = input('Write your age: ')
while int(age) <= 50:
	#15 will be skipped
	if (age == 15):
		age = age + 1
		continue
	if (age == 31):
 #The process in the loop will end
		break
	print ('You have: ' + str(age))
	age = int(age) + 1