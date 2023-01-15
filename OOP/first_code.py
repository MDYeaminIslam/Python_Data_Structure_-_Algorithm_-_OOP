#creating a class
#class is a blueprint for creating objects
#objects are instances of a class

class Person:
    def __init__(self,person_name: str,DOB: str, height:str):
        #self.__age = age #this is private variable. We can't access from outside.Data encapsulation
        self.name = person_name #this is a attribute/instance variable
        self.DOB = DOB
        self.height = height
    
    #this function is belongs to the class
    #instance method
    def get_name(self):
        return self.name

    def set_name(self,new_name):
        if (self.__has_any_number(new_name)):
            print("Sorry person name can't have number")
            return
        self.name = new_name

    def __has_any_number(self,String):
        return "0" in String

    def get_summary(self):
        print(f"Name: {self.name}, DOB: {self.DOB}, Height: {self.height}") #this is string fromating mathod


a_person = Person("Md. Yeamin","22/10/1999","5 feet 7 inches")
b_person = Person("Robert","12/07/1993","6 feet 1 inches")

print(a_person.get_summary())
#print(b_person.get_summary())
a_person.set_name("Md. Yeamin Islam")
print(a_person.get_summary())

#accessing any objects variable
print(a_person.DOB)

a_person.set_name("0Md. Yeamin Islam")
print(a_person.name)
        