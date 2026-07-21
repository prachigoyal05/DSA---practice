def array(arr):
    n = len(arr)
    SN = (n*(n+1))//2
    SN2 = (n*(n + 1) * (2 * n + 1))//6
    S1 = 0
    S2 = 0

    for i in range(n):
        S1+=arr[i]
        S2+= arr[i]*arr[i]

    val1 = S1-SN
    val2 = S2-SN2
    val2 = val2//val1

    x = (val1+val2)//2
    y = x-val1

    return x,y

arr = [2,4,1,3,1,6]
print(array(arr))
        

