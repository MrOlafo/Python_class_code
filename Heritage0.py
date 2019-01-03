class Human:
     def __init__(self, age):
           self.age = age
           print ('I\'m human')
     def talk(self, message):
           print (message)
#init method is inheritance by the other classes
class Engineer(Human):
      def program(self,lenguage):
            print ('I\'m going to program in: ', language)
class Lawyer(Human):
      def studyCase(self,about):
            print ('I\'m going to study the case of: ', about)
#The age is also inherence from the Human class
Gloria = Engineer(21) 
Victoria = Lawyer(28)
Gloria.talk('Hello, Victoria. I\'m ' + str(Gloria.age))
Victoria.talk('Oh! Hi, Gloria. I\'m ' + str(Victoria.age))