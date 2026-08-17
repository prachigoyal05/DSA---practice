def divisors(n):

    for i in range(1,int(n**0.5) + 1):
        if n%i == 0:
            print(i,end = " ")

            if i != n//i:
                print(n//i,end = " ")

n = 36
print(divisors(n))
