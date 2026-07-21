def threeSum(arr):
    arr.sort()
    n = len(arr)
    ans = []

    for i in range(n):
        if i>0 and arr[i] == arr[i-1]:
            continue

        j=i+1
        k=n-1

        while j<k:
            total = arr[i] + arr[j] + arr[k]

            if total<0:
                j+=1

            elif total>0:
                k-=1

            else:
                ans.append([arr[i],arr[j],arr[k]])
                j+=1
                k-=1

                while(j<k and arr[j] == arr[j-1]):
                    j+=1

                while(j<k and arr[k] == arr[k+1]):
                    k-=1

    return ans

arr = [-1,0,1,2,-1,-4]
print(threeSum(arr))

