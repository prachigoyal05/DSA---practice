# class Student:
#     def __init__(self, name):
#         self.name = name

# Student1=Student("Prachi")
# print("student name : ", Student1.name)  

# class Animal:
#     def __init__(self,name):
#         self.name=name
    
#     def sound(self):
#         print(self.name,"makes a sound.")

# class cat(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name)
#         self.breed=breed

#     def details(self):
#         print( self.name, "breed is :", self.breed)

# cat1=cat("Ruhi" ,"Persian")
# cat1.sound()
# cat1.details()

# class Vehicle:
#     def __init__(self,name):
#         self.name=name

#     def type(self):
#         print("The type is: ", self.name)

# class Car(Vehicle):
#     def __init__(self,name,brand):
#         super().__init__(name)
#         self.brand=brand

#     def details(self):
#         print(self.name ,"belongs to ", self.brand)

# car1=Car("SUV","BMW")
# car1.type()
# car1.details()

class Employee:
    def __init__(self,name):
        self.name=name
    def info(self):
        print("The employee name is: ", self.name)

class Intern(Employee):
    def __init__(self,name,domain):
        super().__init__(name)
        self.domain=domain

    def details(self):
        print(self.name, "is mentor of ",self.domain)

E1=Intern("Prachi","ML")
E1.info()
E1.details()

