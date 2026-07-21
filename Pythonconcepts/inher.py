class Parent:
    def __init__(self,Mname,Fname):
        self.Mname=Mname
        self.Fname=Fname

class Child(Parent):
    def __init__(self,Cname):
        self.Cname=Cname
        super().__init__("Pooja","Trilok")

C1=Child("Prachi")
print(C1.Cname," child of", C1.Mname, "and",C1.Fname)

# P1=Parent("Pooja","Trilok")
# print("Parent'name is ",P1.Mname ,"and", P1.Fname)

class Father:
    fathername=" "
    def father(self):
        print("father is", self.fathername)

class Mother:
    mothername=" "
    def mother(self):
        print("mother is",self.mothername)
       

class Child(Father,Mother):
    def parents(self):
        print("mother", self.mothername)
        print("father", self.fathername)

C1=Child()
C1.mothername="Pooja"
C1.fathername="Trilok"
C1.parents()



        