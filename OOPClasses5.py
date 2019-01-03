class Human:
     def __init__(self, age):
           self.age = age
           print ('I am a human being')
     def talk(self, message):
          print (self.age) 
          print (message)
Leslie = Human(23) 
Michael = Human(26)
Leslie.talk('Hello, Michael')
Michael.talk('Oh! Hi, Leslie')
#Talk will execute the age attribute