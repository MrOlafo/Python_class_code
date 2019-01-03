#encoding: utf-8
__author__ = 'AnDr3w-JeY' #The author is Andres J. Jimenez Leandro
#This output allows the user to know what the program does
print("This program is to check the age range of a person\n")
#Opt stands for Option, which is going to be choose by the user
opt = str(input('Do you want to check an age? Write \'S\' for Yes or anyother thing for NO: '))
#This IF is to control the writting of any kind of 'S'
if opt == 'S' or opt == 's':
	#This while works for keep asking for another age
	while opt == 'S' or opt == 's':
		#This try-catch exception works to avoid the use of non-numbers
		try:
			#We require the age to the user 
			age = int(input("Write your age: "))
			if age < 0:
				print("You haven\'t born, yet")
			elif age >= 0 and age < 18:
				print ("You are underage")
			elif age >= 18 and age < 27:
				print ("You are a teenager")
			elif age >= 28 and age < 58 :
				print ("You are an adult")
			#If the person is more than 58 years old, this option will be shown
			else:
				print ("You are elderly old")
			#We request to the user if he wants to try again the program	
			opt = input('Do you want to try another age? Say \'S\' if Yes: ')
		#If user didn't write a number, the exception will be excuted
		except:
			opt = input('That isn\'t a number. Do you want to try again? Write a \'S\': ')		
#The user wants to leave the program, without using it
else:
	print('You didn\'t write a \'S\'. Good Bye!')