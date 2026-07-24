def sqrtNum(n):


    low = 1
    high = n
    ans = 0

    while(low<=high):
        mid = (low+high)//2

        val = mid * mid

        if val <=n:
            ans = mid
            low = mid+1

        else:
            high = mid-1

    return ans

n = 28
print("floor of sqrt of number = ", sqrtNum(n))


