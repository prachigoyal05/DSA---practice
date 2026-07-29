def findDays(weights,capacity):
    days = 1
    load = 0

    for weight in weights:
        if load + weight > capacity:
            days+=1
            load = weight

        else:
            load+=weight


    return days

def minCap(weights,days):
    low = max(weights)
    high = sum(weights)

    while(low<=high):
        mid = (low+high)//2

        reqdays = findDays(weights,mid)

        if reqdays <= days:
            high = mid-1

        else:
            low = mid+1

    return low

weights = [1,2,3,4,5,6,7,8,9,10]
days = 5

print(minCap(weights, days))
