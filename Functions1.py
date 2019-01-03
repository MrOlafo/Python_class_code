__author__ = 'AnDr3w-JeY' #Set the author of the coding
#“def” is a reserve word in Python, that means: ‘define’
def my_function(num1=0, num2=0):
      print(num1+num2)
#After declare my function, I need to execute it:
#Values will be zero
my_function()

#The “num1” will become 3
my_function(3) 
#The “num1” will become 3 and the num2 will become 4
my_function(3,4)
#Same example, but asking the user the numbers:
num1=int(input('Write a number: '))
num2=int(input('Write a number: '))
my_function(num1,num2)