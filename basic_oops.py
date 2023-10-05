class Dog:
    
    #class attribute
    attr = "mammal"
    
    #Instance Attribute
    def __init__(self,name): #In class functions are called method. this is __init__ method
        self.name = name #dynamically assign attributes
    
    def speak(self): #Declaring a method.
        print("I can speak, my name is- {}".format(self.name))

#Driver Code
Rodger = Dog("Rodger") #Object instantiation --> Rodger is an object.

print("Rodger is a {}".format(Rodger.__class__.attr))
print("My name is {}".format(Rodger.name))

#Accessing class methods
Rodger.speak()