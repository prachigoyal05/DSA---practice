# # # class Student:
# # #     def __init__(self,name,marks):
# # #         self.name=name
# # #         self.marks=marks
# # #         print("xyz")


# # # s1 = Student("Prachi", 85)
# # # print(s1.name)
# # # print(s1.marks)

# # # class Student:
# # #     def __init__(self,name,marks):
# # #         self.name=name
# # #         self.marks=marks

# # #     def avg_marks(self):
# # #         sum = 0
# # #         for val in self.marks:
# # #             sum+=val
# # #         print(self.name,"scored",sum/3)
    

# # # s1 = Student("Prachi",[95,99,90])
# # # s1.avg_marks()

# # class Account:
# #     def __init__(self,bal,acc_no):
# #         self.balance=bal
# #         self.account_no=acc_no

# #     def debit(self, amount):
# #         self.balance-=amount
# #         print("Amount debited:", amount)

# #     def credit(self, amount):
# #         self.balance+=amount
# #         print("Amount credited:", amount)

# #     def get_balance(self):
# #         print("total_balance: ",self.balance)

# # acc1 = Account(1000,12345)
# # acc1.debit(500)
# # acc1.credit(1000)
# # acc1.get_balance()

# class Car:
#     @staticmethod
#     def start():
#         print("Car started")

#     @staticmethod
#     def stop():
#         print("car stopped")

# class Toyota(Car):
#     def __init__(self,brand):
#         self.brand=brand

# class Fortuner(Toyota):
#     def __init__(self,type):
#         self.type=type


# # c1 = Fortuner("Petrol")
# # print(c1.start())

# class A:
#     varA = "10"

# class B:
#     varB = "20"

# class C(A,B):
#     varC="30"

# c1=C()
# print(c1.varC)
# print(c1.varA)
# print(c1.varB)

class Car:
    def __init__(self,type):
        self.type=type

    @staticmethod
    def start():
        print("Car started")

    @staticmethod
    def stop():
        print("car stopped")

class Toyota(Car):
    def __init__(self,brand,type):
        super().__init__(type)
        self.brand=brand

car1 = Toyota("fnj","dvdv")
print(car1.type)


    