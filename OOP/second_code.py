# creating a class
# class is a blueprint for creating objects
# objects are instances of a class

class Person:
    #init method acts as the constructor
    #we type casting like below for avoid unnatural circumtances
    #here in height value it's a optional variable because of using None word
    def __init__(self, person_name: str, year_of_birth: int, height:int = None):
        # self.__age = age #this is private variable. We can't access from outside.Data encapsulation
        self.__name = person_name  # this is a attribute/instance variable
        self.__year_of_birth = year_of_birth
        self.__height = height

    # this function is belongs to the class
    # instance method
    def get_name(self):
        return self.__name

    def get_year_of_birth(self):
        return self.__year_of_birth

    def set_name(self, new_name: str):
        if (self.__has_any_number(new_name)):
            print("Sorry person name can't have number")
            return
        self.__name = new_name

    def __has_any_number(self, String: str):
        return "0" in String

    def get_summary(self):
        print(f"Name: {self.__name}, DOB: {self.__year_of_birth}, Height: {self.__height}")  # this is string fromating mathod


person_List = []
person_List.append(Person("Md. Yeamin Islam",1998,72))
person_List.append(Person("Rafiqul Alom",1992))
person_List.append(Person("Md.Rabiul Islam",1966,23))
person_List.append(Person("Sahara Khatun",1989,69))
person_List.append(Person("Shohidul Islam",2000,72))
person_List.append(Person("Sourov Mia",1999,82))

for person in person_List:
    if (person.get_year_of_birth() >= 1990):
        print(person.get_summary())


#creatinf a new class
class Student(Person):
    #here we import Person class parameters
    def __init__(self, person_name: str, year_of_birth: int,Email_ID: str, student_ID: str):
        super().__init__(person_name, year_of_birth)
        self.id = student_ID
        self.email_ID = Email_ID

    def get_summary(self):
        return f"Name: {self.get_name()}, Email: {self.email_ID}, Birth: {self.get_year_of_birth()}"

    #this string method will convert the value into string
    def __str__(self):
        return self.get_summary()

    def __repr__(self):
        return self.get_summary()

student = Student("Abdur Rahim",2000,"rahim12-1223@gmail.com","211-15-1244")
print(student.get_summary())
student.set_name("Abdur Rahim Rabbi")
print(student.get_summary())


class Teacher(Person):
    def __init__(self, person_name: str, year_of_birth: int, department: str):
        super().__init__(person_name, year_of_birth)
        self.department = department

new_person_list = [Person("Yeamin", 1993),Student("Rakin",2001,"rakin@gmail.com","2343-34-34"),Teacher("Safayet",1978,"Science")]
for p in new_person_list:
    print(p.get_name())
    print(p.get_summary())