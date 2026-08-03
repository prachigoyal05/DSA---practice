def revString(str):
    s = list(str)
    left = 0
    right = len(s)-1

    while(left<right):
        s[left],s[right] = s[right],s[left]
        right-=1
        left+=1

    return "".join(s)
str = "hello"
print("reversed string = ",revString(str))


