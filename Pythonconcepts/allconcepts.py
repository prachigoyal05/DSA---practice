from abc import ABC,abstractmethod
class Animal(ABC):
    def __init__(self,name):
        self.__name=name
    @abstractmethod
    def sound(self):
        print("Generic sound")

    def show_name(self):
        print(self.__name)


class Dog(Animal):
    def sound(self):
        print("bark")

class Cat(Animal):
    def sound(self):
        print("meow")

animals=[Dog("Buddy"), Cat("Whiskers")]
for i in animals:
    i.sound()
    i.show_name()



class Animal:
    def sound(self):
        print("generic")


class Dog(Animal):
    def sound(self):
        print("bark")

animals = [Dog(),Animal()]
for i in animals:
    i.sound()