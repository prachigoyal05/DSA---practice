def find_secondLargest_secondSmallest(arr):
    largest = arr[0]
    sslargest = float('-inf')

    smallest = arr[0]
    ssmallest = float('inf')

    n = len(arr)

    for i in range(0,n):
        if arr[i] > largest:
            sslargest = largest
            largest = arr[i]

        elif arr[i] < largest and arr[i] > sslargest:
            sslargest = arr[i]

        if arr[i] < smallest:
            ssmallest = smallest
            smallest = arr[i]

        elif arr[i] > smallest and arr[i] < ssmallest:
            ssmallest = arr[i]

    return sslargest, ssmallest

arr = [5, 2, 8, 1, 9]
sslargest,ssmallest = find_secondLargest_secondSmallest(arr)
print("second largest : ", sslargest)
print("second smallest : ", ssmallest)

        
