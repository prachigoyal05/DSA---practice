age = int(input("Enter your age: "))
if(age>=21):
    print("You are an eligible adult")
else:
    print("Well you have to wait to be an adult")
# -------------
marks = 101
if(marks>=90):
    if(marks>=100):
        grade = "B"
    else:
        grade = "A"
    
else:
    grade = "D"
print("grade of the student: ",grade)

# ---------
no = int(input("Enter a number: "))
if(no%2==0):
    print("The number is even")
else:
    print("odd")
# -------------------
# first = int(input("enter the first no:"))
# second = int(input("enter the second no:"))
# third = int(input("enter the third no:"))

# if(first>second and first>third):
#     print("first is the greatest")
# elif(second>first and second>third):
#     print("second is the greatest")
# else:
#     print("third is the greatest")

# ---------------
num = 4

if(num%7==0):
    print("num is multiple of 7")
else:
    print("lol")
