def maxSubarray(arr):
    maxi = float('-inf')
    current_sum = 0

    start = 0
    tempstart = 0
    end = 0

    for i in range(len(arr)):
        current_sum += arr[i]

        if current_sum > maxi:
            maxi = current_sum
            start = tempstart
            end = i

        if current_sum < 0:
            current_sum = 0
            tempstart = i+1

    print("maxSubarray", maxi)
    print("elements", arr[start:end+1])

    return maxi

arr = [-2,1,-3,4,-1,-2,1,5,-4]
print(maxSubarray(arr))