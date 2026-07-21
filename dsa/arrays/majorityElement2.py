
def majorityElement(nums):
    n = len(nums)
    cnt1 = 0
    cnt2 = 0
    el1 = 0
    el2 = 0

    for num in nums:
        if cnt1 == 0 and el2 !=num:
            el1 = num
            cnt1 = 1

        elif cnt2 == 0 and el1 != num:
            el2 = num
            cnt2 = 1

        elif num == el1:
            cnt1+=1

        elif num == el2:
            cnt2+=1

        else:
            cnt1-=1
            cnt2-=1


    cnt1 = 0
    cnt2 = 0

    for num in nums:
        if num == el1:
            cnt1+=1

        if num == el2:
            cnt2+=1


    mini = n//3 + 1

    result = []

    if cnt1>=mini:
        result.append(el1)

    if cnt2>=mini:
        result.append(el2)

    return result

nums = [3,3,2,2,1,2,4,3]
print(majorityElement(nums))