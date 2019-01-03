class Human:
     def __init__(self):
           print ('I am a human being')
     #Self connects a method with it class on an object
     def talk(self, message):
           print (message)
Male = Human() #Object1
Female = Human() #Object2
Female.talk('Hello, my name is Martha')
Male.talk('Hi, my name is John')