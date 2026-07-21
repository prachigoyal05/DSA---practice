def linear_search(arr,num):
    for i in range (0,len(arr)):
        if arr[i] == num:
            return i
    return -1

arr = [1, 2, 3, 4, 5]
print(linear_search(arr,6))