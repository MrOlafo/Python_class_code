class Human:
  def __init__(self, age):
    self.age = age
    print ('I\'m human')
  def talk(self, message):
    print (message)
class Engineer(Human):
  def __init__(self):
    print('Hello')
  def program(self,lenguage):
    print ('I\'m going to program in: ', lenguage)
class Lawyer(Human):
  def __init__ (self,college):
    print('Lawyer from the: ', college)
  def studyCase(self,about):
    print ('I\'m going to study the case of: ', about)
#Multiple heredity class
class Student(Engineer,Lawyer):
#Human class inheritance are already included in the multiple heredity, because both parent classes, receives heritage from the super-class Human
  pass #Passing without adding any other method
Peter = Engineer() 
Thomas = Lawyer(28)
Luke = Student()
Luke.talk('Hello')
Luke.program('Java')
Luke.studyCase('Marriage')