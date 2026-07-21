def longestSubarray(arr,k):
    n = len(arr)
    left = 0
    right = 0
    sum = arr[0]
    maxL = 0

    while right < n:

        while left<=right and sum>k:
            sum-=arr[left]
            left+=1

        if sum == k:
            maxL = max(maxL,right - left + 1)

        right+=1
        if right<n:
            sum+=arr[right]

    return maxL

arr = [1, 2, 3, 4, 5]
print(longestSubarray(arr,9))
