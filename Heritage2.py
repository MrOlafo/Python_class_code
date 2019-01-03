class Human:
     def __init__(self, age):
           self.age = age
           print ('I\'m human')
     def talk(self, message):
           print (message)
class Engineer(Human):
#It overwrites the heirdom method from Human class     
     def __init__(self):
           print('Hello')
     def program(self,lenguage):
            print ('I\'m going to program in: ', lenguage)
class Lawyer(Human):
      def studyCase(self,about):
            print ('I\'m going to study the case of: ', about)
Gloria = Engineer() 
Victoria = Lawyer(28)
Gloria.program('Python')
Victoria.studyCase('Adoption')
Gloria.talk('Hello')
Victoria.talk('Hi')