import heapq
def highestProd(li):
    h1, h2 = [], []
    for i, l in enumerate(li):
        if l < 0:
            if len(h2) < 2:
                heapq.heappush(h2, abs(l))
            elif h2[0] < abs(l):
                heapq.heappop(h2)
                heapq.heappush(h2, abs(l))
        if len(h1) < 3:
            heapq.heappush(h1, l)
        elif h1[0] < l:
            heapq.heappop(h1)
            heapq.heappush(h1, l)
    prod1 = h1[0] * h1[1] * h1[2]
    prod2 = max(h1) * h2[0] * h2[1] if len(h2) == 2 else float('-inf')
    return max(prod2, prod1)


print highestProd([1, 2, 3, 4, 5])
print highestProd([-10, -10, 1, 2, 3])
print highestProd([-10, 1, 0, 0])


