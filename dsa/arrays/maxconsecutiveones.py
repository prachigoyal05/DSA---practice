def maxConsOnes(arr):
    maxi = 0
    cnt = 0
    for i in range(len(arr)):
        if arr[i] == 1:
            cnt+=1
            maxi = max(maxi,cnt)

        else:
            cnt = 0

    return maxi

arr = [1, 1, 0, 1, 1, 1]
print(maxConsOnes(arr))


