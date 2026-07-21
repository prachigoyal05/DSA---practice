def nextgap(gap):
    if gap <= 1:
        return 0 
    
    return (gap//2)+(gap%2)

def mergeArray(arr1,arr2):

    n = len(arr1)
    m = len(arr2)

    length = m+n
    gap = nextgap(length)

    while gap > 0:
        left = 0
        right = left+gap

        while right<length:
            if left < n and right < n:
                if arr1[left] > arr1[right]:
                    arr1[left],arr1[right] = arr1[right],arr1[left]

            elif left < n and right >= n:
                if arr1[left] > arr2[right-n]:
                    arr1[left],arr2[right-n] = arr2[right-n],arr1[left]

            #both in array 2
            else: 
                if arr2[left-n] > arr2[right-n]:
                    arr2[left-n],arr2[right-n] = arr2[right-n],arr2[left-n]

            left+=1
            right+=1

        gap = nextgap(gap)

    return arr1,arr2

arr1 = [1,4,8,10]
arr2 = [2,3,9]

print(mergeArray(arr1, arr2))