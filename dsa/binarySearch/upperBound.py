def upperBound(arr,x):
    n = len(arr)
    low = 0
    high = n-1

    ans = n

    while(low<=high):
        mid = (high+low)//2
        if arr[mid]>x:
            ans = mid
            high = mid-1

        else:
            low = mid+1

    return ans

arr = [2,4,7,9,12]
print(upperBound(arr,12))