def floorAndCeil(arr,x):
    n = len(arr)
    low = 0
    high = n-1
    ceil = -1
    floor = -1

    while(low<=high):
        mid = (low+high)//2

        if arr[mid] == x:
            ceil = arr[mid]
            floor = arr[mid]
            break

        elif arr[mid]>x:
            ceil = arr[mid]
            high = mid-1

        else:
            floor = arr[mid]
            low = mid+1

    return floor,ceil

arr = [2,4,6,8,14]
print(floorAndCeil(arr,5))

