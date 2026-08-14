def palindrome(n):
    rev = 0
    dupl = n
    while n > 0:
        
        digit = n%10
        rev = rev * 10 + digit

        n = n//10

    if rev == dupl:
        return True
    return False

n = 1331
print(palindrome(n))



