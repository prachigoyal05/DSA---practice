class Animal:
    def sound(self):
        print("Generic")

class Dog(Animal):
    def sound(self):
        print("bark")

class Cat(Animal):
    def sound(self):
        print("meow")

animals=[Dog(),Cat(),Animal()]
for i in animals:
    i.sound()

