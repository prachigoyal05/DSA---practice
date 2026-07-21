def majorityElement(arr):

    candidate = 0
    count = 0

    for i in range(len(arr)):
        if count == 0:
            candidate = arr[i]
            count = 1

        elif arr[i] == candidate:
            count+=1

        else:
            count-=1

    return candidate

arr = [3,2,3]
print(majorityElement(arr))

        