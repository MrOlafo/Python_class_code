try:
	start=input('Welcome to the Studen Grade System. Press 1 to continue or 0 to leave: ')
	start=(int(start))
	while start!=1 and start!=0:
		start=input('Please press 1 to continue or 0 to leave: ')
		start=(int(start))	
	if start==1:
		while start==1:
			grade=input('Type the grade of the student in a range of 1 to 100. Been 1 the lowest and 100 the highest: ')
			grade=(int(grade))
			while grade<=0 or grade>100:
				grade=input('The grade must be in a range of 1 to 100. Been 1 the lowest and 100 the highest. Plese type the grade again: ')
				grade=(int(grade))
			if grade==100 or grade>=91:
				print('The grade is A. This student pass the course.')
			else:
				if grade==90 or grade>=71:
					print('The grade is B. This student pass the course.')
				else:
					if grade==70 or grade>=61:
						print('The grade is C. This student did not pass the course.')
					else:
						if grade==60 or grade>=50:
							print('The grade is D. This student did not pass the course.')
						else:
							print('The grade is E. This student did not pass the course.')
			start=input('Do you want to grade another student? Yes=1 No=0: ')
			start=(int(start))
			while start!=1 and start!=0:
				start=input('Please press 1 to continue or 0 to leave: ')
				start=(int(start))											
	print('Thanks for using the Student Grade System. Bye')			
except:
	print('Use numbers, not letters')