def singleElement(arr):
    n = len(arr)
    low = 0
    high = n-1

    if n == 1:
        return arr[0]
    
    if arr[0]!=arr[1]:
        return arr[0]

    if arr[n-2] != arr[n-1]:
        return arr[n-1]
    
    while low<=high:

        mid = (low+high)//2

        if arr[mid]!=arr[mid-1] and arr[mid]!=arr[mid+1]:
            return arr[mid]
        
        if (mid%2 == 1 and arr[mid] == arr[mid-1]) or (mid%1 == 0 and arr[mid] == arr[mid+1]):
            low = mid+1

        else:
            high = mid-1

    return -1 

arr = [1,1,2,2,3,3,4,5,5]
print(singleElement(arr))

