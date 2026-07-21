def zeroes_to_end(arr):
    n = len(arr)

    j = -1

    for i in range(0,n):
        if arr[i] == 0:
            j = i
            break

    for i in range(j+1,n):
        if arr[i]!=0:
            arr[i],arr[j]= arr[j],arr[i]
            j+=1

    return arr

arr = [1, 0, 2, 0, 3, 4, 0]
print(zeroes_to_end(arr))

