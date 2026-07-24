import math
def totalhours(piles,speed):
    total = 0
    for pile in piles:
        total+=math.ceil(pile/speed)

    return total

def minTime(arr,h):
    low = 1
    high = max(arr)

    while low<=high:
        mid = (low+high)//2

        total = totalhours(arr,mid)

        if total<=h:
            high = mid-1

        else:
            low = mid+1

    return low

piles = [3,6,7,11]
print("min time = ",minTime(piles,8))
