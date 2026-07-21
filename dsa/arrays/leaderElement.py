def LeaderElement(arr):
    n = len(arr)
    maxi = float('-inf')

    ans = []

    for i in range(n-1,-1,-1):
       
       if arr[i]>maxi:
           ans.append(arr[i])
           maxi = arr[i]

    arr.reverse()
    return ans
arr = [16, 17, 4, 3, 5, 2]
print(LeaderElement(arr))