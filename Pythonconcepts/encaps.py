# ENCAPSULATION
class Employee:
    def __init__(self,name,salary,bonus):
        self.name=name
        self.__salary=salary #private attribute cant be accessesed directly
        self._bonus=bonus

    def show_salary(self):
        print("salary", self.__salary)

class Manager(Employee):
    def show_bonus(self):
        print("bonus : ", self._bonus)

# e1=Employee("Prachi",100000)
e1=Manager("Prachi",100000,20000)
print(e1.name)
e1.show_salary() #can access through method of same classs but not directly
 #print(e1.__salary)will show error
e1.show_bonus() #protected attrubute accessed in sub class