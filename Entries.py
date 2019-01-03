#The input NEEDS to be "saved" on a variable, because is a data that the user inputs from keyboard
valor=input()
#All value that comes from the user's keyboard is automatically consider as a string by Python
print(type(valor))
#We print it as any other string
print(valor)
"""To make it an integer, we should firstly ask for a number, make sure the user will write a number, and the 
cast the variable into a integer type"""
try:
	#To avoid values issues when expecting an integer and receving a letter. we just create a try-catch exception
	valor=input("Write a Number:")
	#The value changes to integer
	valor=(int(valor))
except:
	print("That isn\'t a number")
else:
	print(valor)