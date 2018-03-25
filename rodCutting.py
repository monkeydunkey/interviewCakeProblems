def cutRods(priceArr, LenArr, n):
    maxProfit = [0]
    for i in range(n):
        #iterating over all the possible length
        maxPartProfit = 0
        for x in range(len(priceArr)):
            profit = priceArr[x] + maxProfit[i -x] if i - x >= 0 else 0
            maxPartProfit = max(maxPartProfit, profit)
        maxProfit.append(maxPartProfit)
    return maxProfit[-1]


print cutRods([1,5,8,9,10,17,17,20], [1,2,3,4,5,6,7,8], 8)
