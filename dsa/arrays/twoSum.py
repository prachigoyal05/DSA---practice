def twoSum(arr,target):
    n = len(arr)
    hashmap = {}

    for i in range(n):

        complement = target-arr[i]

        if complement in hashmap:
            return hashmap[complement],i
        
        hashmap[arr[i]] = i

    return []

arr = [2,7,11,15]
print(twoSum(arr,17))
