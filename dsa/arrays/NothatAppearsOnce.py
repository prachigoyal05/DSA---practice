def appearOnce(arr):
    xor = 0
    for i in range(len(arr)):
        xor^=arr[i]

    return xor

arr = [1, 2, 3, 3, 1]
print(appearOnce(arr))