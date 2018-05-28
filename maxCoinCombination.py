def maxCoinComb(amt, coins):
    amt_till_now = [0] * (amt + 1)
    amt_till_now[0] = 1
    for c in coins:
        for i in xrange(c, amt + 1):
            rem = i - c
            amt_till_now[i] += amt_till_now[rem]
    return amt_till_now[-1]


print maxCoinComb(4, [1,2,3])
print maxCoinComb(4, [5, 6, 7])
print maxCoinComb(2, [1, 2, 3])

