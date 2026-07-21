def binarySearch(arr,target):
    n = len(arr)
    low = 0
    high = n-1
    while(low<=high):
        mid = (low+high)//2
        if arr[mid] == target:
            return mid

        elif target>arr[mid]:
            low = mid+1

        else:
            high = mid-1

    return -1

arr = [3, 4, 6, 7, 9, 12, 16, 17]
print(binarySearch(arr,12))