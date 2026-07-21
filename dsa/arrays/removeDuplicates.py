def remove_duplicates(arr):
    if len(arr) == 0:
        return arr
    
    i = 0
    for j in range(1,len(arr)):
        if arr[i]!=arr[j]:
            arr[i+1]=arr[j]
            i+=1

    return i + 1

arr = [1, 1, 2, 3, 3, 4]
new_length = remove_duplicates(arr)

print(new_length)


