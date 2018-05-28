'''
The world-known gangster Vito Deadstone is moving to New York. He has a very big family there, all
of them living in Lamafia Avenue. Since he will visit all his relatives very often, he is trying to find a house close to them.
Vito wants to minimize the total distance to all of them and has blackmailed you to write a program
that solves his problem.
We need to find the value that has the least sum of abs diff with all the elements of the array
'''

def findMin(arr):
    arr = sorted(arr)
    return arr[len(arr) / 2]


print findMin([2,2,4])
print findMin([3, 2, 4, 6])

