class Human:
     def __init__(self):
           self.age = 25 #This an attribute
           print ('I am a human being')
     def talk(self, message):
           print (message)
Leslie = Human() 
Michael = Human()
Leslie.talk('Hello, Michael')
Michael.talk('Oh! Hi, Leslie')
print ('I have ' + str(Michael.age) + 'years old')