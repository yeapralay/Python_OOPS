class Item:
    def __init__(self,name,price,quantity):
        self.name = name #Declaring attributes
        self.price = price
        self.quantity = quantity
        
        print(f'An instance created:{name}')
        
    def calculate_sum(self): #declaring a method
        return self.price * self.quantity # --> Have access to all the attributes of the class


item1 = Item('pen',10,100) # making an object --> object itself passed as an argument
item2 = Item('pencil',5,20)

print(item1.name)
print(item2.name)
print(item1.price)
print(item2.price)
print(item1.quantity)
print(item2.quantity)

print('+++++++++++++++++++++++ Printing Sum ++++++++++++++++++')
print(item1.calculate_sum())
print(item2.calculate_sum())