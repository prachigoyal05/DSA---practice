# # class Circle:
# #     def __init__(self,radius):
# #         self.radius=radius

# #     def area(self):
# #         return 3.14*self.radius*self.radius
    
# #     def perimeter(self):
# #         return 2*3.14*self.radius

# # c1=Circle(21)
# # print("AREA of circle : ",c1.area())
# # print("Perimeter of circle :", c1.perimeter())

# class Employees:
#     def __init__(self,role,department,salary):
#         self.role=role
#         self.department=department
#         self.salary=salary

#     def showDetails(self):
#         print("role = ", self.role)
#         print("department = ", self.department)
#         print("salary = ", self.salary) 


# class Engineer(Employees):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         super().__init__("software engineer","It","2,00,000")

# # e1=Employees("software engineer","It","2,00,000")
# # e1.showDetails()

# e2=Engineer("Alice", 30)
# # print("Name = ", e2.name)
# # print("Age = ", e2.age)
# e2.showDetails()

class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price