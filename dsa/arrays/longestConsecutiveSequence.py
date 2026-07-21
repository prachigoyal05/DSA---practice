def longestSeq(arr):
    if len(arr)==0:
        return 0

    nums = set(arr)

    longest = 1

    for num in nums:
        if num-1 not in nums:
            current = num
            count=1

            while current+1 in nums:
                current+=1
                count+=1
            longest = max(longest,count)

    return longest

arr = [100, 4, 200, 1, 3, 2]
print(longestSeq(arr))
