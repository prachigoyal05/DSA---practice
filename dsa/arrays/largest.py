def find_largest(arr):
    largest = arr[0]
    n=len(arr)
    for i in range(0,n):
        if arr[i]>largest:
            largest=arr[i]

    return largest
arr = [5, 2, 8, 1, 9]   
print(find_largest(arr))
