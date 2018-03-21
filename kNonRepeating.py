def kNonRepeating(st, k):
   charCount = {}
   for i, s in enumerate(st):
       if charCount.get(s, None) is None:
            charCount[s] = i
       else:
            charCount[s] = -1
   i = 0
   arr = sorted(filter(lambda x: x[1] !=-1, charCount.items()), key = lambda x: x[1])
   if len(arr) < k :
       return 'Kth smallest not available'
   else:
       return arr[k-1][0]


if __name__ == '__main__':
    s = 'geeksforgeeks'
    print kNonRepeating(s, 3)
    print kNonRepeating(s, 2)
    print kNonRepeating(s, 4)
