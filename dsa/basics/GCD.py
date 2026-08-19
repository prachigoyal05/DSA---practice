def GCD(a,b):
    while a>0 and b>0:
        if a>b:
            a = a%b

        else:
            b = b%a

    if a == 0:
        return b

    return a

a = 3
b = 9
print(GCD(a,b))
