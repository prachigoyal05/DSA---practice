def is_sorted(n,arr):

    for i in range(1,n):
        if arr[i] < arr[i-1]:
            return False

    return True

arr = [2, 4, 6, 7, 9]
n = len(arr)


if is_sorted(n,arr):
    print("The array is sorted.")

else:
    print("not sorted")               