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
  def __init__ (self,college, args):
    super(Human).__init__(type(args))
    print('Age: ',args)
    print('Lawyer from the: ', college)
  def studyCase(self,about):
    print ('I\'m going to study the case of: ', about)
#Altered order, brings altered init functions priorities
class Student(Lawyer,Engineer):
  pass
Luke = Student('UTN',28)
Luke.talk('Hello')
Luke.program('Java')
Luke.studyCase('Marriage')