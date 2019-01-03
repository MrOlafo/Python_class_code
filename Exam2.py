#With this try we are avoiding that the users use letters instead of numbers
try:
#The program starts runnig. The user should press 1 to continue or 0 to leave	
	start=input('Welcome to the Studen Grade System. Press 1 to continue or 0 to leave: ')
	start=(int(start))
#Verify that the user did not write down a invalid value for the program. Only 1 or 0 are valid.	
	while start!=1 and start!=0:
		start=input('Please press 1 to continue or 0 to leave: ')
		start=(int(start))
#If the variable start is equal to 1, the system starts the grade conversion
	if start==1:
#While start is equal to 1, the system stays in the grade conversion
		while start==1:
			grade=input('Type the grade of the student in a range of 1 to 20. Been 1 the lowest and 20 the highest: ')
			grade=(int(grade))
#Verify that the users write down a valid grade. If not, the system will continue asking for a valid grade range 			
			while grade<=0 or grade>20:
				grade=input('The grade must be in a range of 1 to 20. Been 1 the lowest and 20 the highest. Plese type the grade again: ')
				grade=(int(grade))
#Begins the grade convertion, A=20 or 19, B=18, 17 or 16, C=15, 14 or 13, D=12, 11 or 10, E=9 to 1				
			if grade==20 or grade==19:
				print('The grade is A.')
			else:
				if grade==18 or grade>=16:
					print('The grade is B.')
				else:
					if grade==15 or grade>=13:
						print('The grade is C.')
					else:
						if grade==12 or grade>=10:
							print('The grade is D.')
						else:
							print('The grade is E.')
#The system ask the user to continue converting grades or leave the program							
			start=input('Do you want to grade another student? Yes=1 No=0: ')
			start=(int(start))
#Verify that the user did not write down a invalid value for the program. Only 1 or 0 are valid.			
			while start!=1 and start!=0:
				start=input('Please press 1 to continue or 0 to leave: ')
				start=(int(start))											
	print('Thanks for using the Student Grade System. Bye')	
#If the users write down a letter the program will be finalized		
except:
	print('Use numbers, not letters')