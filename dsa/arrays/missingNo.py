def find_missingno(arr,N):
    xor1 = 0
    xor2 = 0
    n = len(arr)

    for i in range(N-1):
        xor2^=arr[i]
        xor1^=(i+1)

    xor1^=N
    return xor1^xor2

arr = [1, 2, 3, 5]
print(find_missingno(arr,5))

