class Item:
    
    # There is two types of attributes in python -- 1. Classs Attribute & 2. Instance Attribute
    
    # The Pay rate after 20% discount
    pay_rate = 0.8 # Declaring attributes --> Class Attributes
    
    def __init__(self,name:str,price:float,quantity=0): # declaring types of the passing attributes 
        
        #Run validations to the received arguments
        
        assert price >= 0 #assert used for checking conditions --> if condition returns True, then nothing happens 
                          #but if condition returns False, AssertionError is raised
        assert quantity >= 0 ,f"Quantity {quantity} is not greater or equal to the zero."
        
        #Assign to self object
        self.name = name #Declaring attributes -- Instance Attributes
        self.price = price
        self.quantity = quantity
        
        print(f'An instance created:{name}')
        
    def calculate_sum(self): #declaring a method
        return self.price * self.quantity # --> Have access to all the attributes of the class


item1 = Item('pen',10,100) # making an object --> object itself passed as an argument
item2 = Item('pencil',5,20)

print(item1.pay_rate)
print(Item.pay_rate)

print(Item.__dict__) #All the attributes of Class level
print(item1.__dict__) # All the attributes for instanbce level