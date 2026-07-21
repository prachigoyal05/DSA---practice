def fourSum(arr,target):
    arr.sort()
    n = len(arr)
    ans = []

    for i in range(n):
        if i>0 and arr[i] == arr[i-1]:
            continue

        for j in range(i+1,n):
            if j>i+1 and arr[j] == arr[j-1]:
                continue


            k = j+1
            l = n-1

            while k<l:
                total = arr[i] + arr[j] + arr[k] + arr[l]

                if total == target:
                    ans.append([arr[i],arr[j],arr[k],arr[l]])
                    k+=1
                    l-=1

                    while(k<l and arr[k] == arr[k-1]):
                        k+=1

                    while(k<l and arr[l] == arr[l+1]):
                        l-=1
                
                elif total > target:
                    l-=1

                else:
                    k+=1

    return ans

arr = [1,1,-4,5,-3,-2,2,1]
print(fourSum(arr,0))
