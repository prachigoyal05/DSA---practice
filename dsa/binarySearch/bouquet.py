def possible(arr,day,m,k):
    count = 0
    bouquet = 0

    for bloom in arr:
        if bloom <= day:
            count+=1

        else:
            bouquet+=count//k
            count = 0

    bouquet+=count//k
    return bouquet>=m

def minBouquet(arr,m,k):
    n = len(arr)

    if n < m*k:
        return -1
    
    low = min(arr)
    high = max(arr)

    while(low<=high):
        mid = (low+high)//2

        if possible(arr,mid,m,k):
            high = mid-1

        else:
            low = mid+1

    return low

arr = [7,7,7,7,13,12,11,7]
print("min bouquets = ",minBouquet(arr,2,3))
