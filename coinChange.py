def coinChange(coins, totalAmount):
    amountArr = [[0 for x in coins] for y in range(totalAmount + 1)]
    for i in range(len(coins)):
        amountArr[0][i] = 1
    for i in range(1, totalAmount + 1):
        for j, c in enumerate(coins):
            x = amountArr[i - c][j] if i - c >= 0 else 0
            y = amountArr[i][j-1]
            amountArr[i][j] = x + y
    return amountArr[-1][-1]


print coinChange([1,2,3], 4)
print coinChange([2, 5, 3, 6], 10)
