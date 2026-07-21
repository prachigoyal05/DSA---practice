# def calc_sum(a,b):#parameters
#     sum = a+b
#     print(sum)
#     return sum

# calc_sum(3,5) @arguements

# calc_sum(7,10)

# def calc_avg(a,b,c):
#     avg = (a+b+c)/3
#     print(avg)
#     return avg

# calc_avg(2,4,6)

# list1 = ["cat", "dog", "rabbit", "bird", "fish"]

# # def calc_len(list):
# #     print(len(list))

# # calc_len(list1)
# def calc_list(list):
#     for i in list:
#         print(i, end=" ")

# calc_list(list1)

# def calc_fact(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact=fact*i
#     print(fact)

# calc_fact(5)

#recursion
def show(n):
    if (n==0):
        return
    print(n)
    show(n-1)
    print("end")


show(5)
