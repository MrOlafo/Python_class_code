__author__ = 'AnDr3w-JeY' #Set the author of the code
#Using Return on a Function
def my_function(num1, num2):
      return(num1 + num2)
#Save result in a variable:
result_ofSumm = my_function(3,4)
print(result_ofSumm)
#Same example, but asking the user the numbers:
num1=int(input('Write a number: '))
num2=int(input('Write a number: '))
resultOfSumm = my_function(num1,num2)
print(resultOfSumm)