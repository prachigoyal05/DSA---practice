i = 1
while i<=5:
    print("Hello")
    i+=1
n=int(input("Enter a number "))
i = 1
while i<=10:
    print(n*i)
    i+=1

nums = (1,4,9,16,25,36,49,64,81,100)
x = 16
i=0
while i <len(nums):
    if nums[i] == x:
        print("found",i)
        break
    else:
        print("yet to find",i)
    i+=1

print("End of loop")

# i = 1
# while i<=5:
#     if i==3:
#         i+=1
#         continue
#     print(i)
#     i+=1

# i=1
# while i<=10:
#     if i%2==0:
#         i+=1
#         continue
#     print("odd no:", i)
#     i+=1

# list = [1,4,9,16,25,36,49,64,81,100]
# for i in list:
#     print(i)

list = [1,4,9,16,25,36,49,64,81,100]  
x = 36
for i in list:
    if i==x:
        print("found", i)
        break 
    print("finding") 

for i in range(100,0,-1):
    print (i)

n=int(input("Enter a number "))
for i in range(1,11):
    print(n*i)

for i in range(5):
    pass

print("nothing")

n=int(input("Enter n "))
sum = 0 
i = 0
while i<=n:
    sum += i
    i+=1

print(sum)

n = 5
fact = 1
for i in range(1,n+1):
    fact = fact*i
    i+=1
print(fact)




