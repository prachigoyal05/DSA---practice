def maxProfit(prices):
    mini = prices[0]
    max_profit = 0

    for i in range(len(prices)):

        profit = prices[i]-mini
        max_profit = max(profit, max_profit)

        mini = min(mini,prices[i])

    return max_profit
arr = [7,1,5,3,6,4]
print(maxProfit(arr))