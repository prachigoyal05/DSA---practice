def isArmstrong(n):
    duplic = n
    digits = len(str(n))
    sum = 0

    while n > 0:
        digit = n%10

        sum = sum + digit ** digits

        n = n//10

    if duplic == sum:
        return True

    return False

n = 153
print(isArmstrong(n))

