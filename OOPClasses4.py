class Human:
     def __init__(self, age):
    #self.attribute = variable
           self.age = age
           print ('I am a human being')
     def talk(self, message):
           print (message)
Leslie = Human(23) 
Michael = Human(26)
Leslie.talk('Hello, Michael')
Michael.talk('Oh! Hi, Leslie')
print ('I\'m Michael, and I have ' + str(Michael.age) + ' years old')
print ('I\'m Leslie, and I have ' + str(Leslie.age) + ' years old')