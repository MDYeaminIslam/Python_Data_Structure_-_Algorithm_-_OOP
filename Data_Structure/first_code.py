class Dog:
    #Represnets a dog class
    #this innit fuction will create objects of class Dog
    def __init__(self,_name,_age,_color):
        self.name = _name
        self.age = _age
        self.color = _color
        
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def get_color(self):
        return self.color
    
    #this bark is method of class Dog
    def bark(self):
        print("Huff! Huff!..")
        

#creating instance giving value to them
mydog = Dog("Tommy",3,"Brown")
mydog.bark()
print(mydog.get_name())
print(mydog.get_age())
print(mydog.get_color())
