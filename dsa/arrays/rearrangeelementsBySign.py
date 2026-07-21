def rearrangedArray(arr):
    ans = [0]*len(arr)

    posIndex = 0
    negIndex = 1

    for i in range(len(arr)):
        if arr[i] < 0:
            ans[negIndex] = arr[i]
            negIndex+=2

        else:
            ans[posIndex] = arr[i]
            posIndex+=2

    return ans

arr = [3, 1, -2, -5, 2, -4]
print(rearrangedArray(arr))

