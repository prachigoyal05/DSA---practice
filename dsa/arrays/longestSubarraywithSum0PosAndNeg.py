def longestSubarray(arr):
    n = len(arr)
    max_len = 0
    prefix_sum = 0
    hashmap = {}

    for i in range(n):
        prefix_sum+=arr[i]

        if prefix_sum == 0:
            max_len = i+1

        elif prefix_sum in hashmap:
            length = i-hashmap[prefix_sum]
            max_len = max(max_len,length)

        else:
            hashmap[prefix_sum] = i

    return max_len

arr = [1, 2, -3, 3, -1, 2, -2]
print(longestSubarray(arr))
        


                    