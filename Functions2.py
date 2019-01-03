__author__ = 'AnDr3w-JeY’ #Set the author of the code'
#“def” is a reserve word in Python, that means: ‘define’
def my_function(cad, v=2):
      print(cad*v)
#After declare my function, I need to execute it:
#The “cad” will become ‘Python ’
my_function('Python ')
#The “cad” will become ‘Python ’ and the v will become 5
my_function('Python ',5)

#Everything after the ‘*’ will become a Tuple:
def my_function2(cad, v=2,*somethingMore):
      print(cad*v)
#We will use a ‘for’ type of loop to roam the Tuple
      for cadena in somethingMore:
           print(cadena * v)
#This will execute all my declare strings
my_function2('Python ',5,'Hi ','Bye ','N ','strings ')
#This will only execute the first print, it won’t go into the for, because there aren’t “data” for that “somethingMore” variable
my_function2('Python ',5)
#Execute in Terminal