# Time:  O(1)
# Space: O(1)

# Given a time represented in the format "HH:MM",
# form the next closest time by reusing the current digits.
# There is no limit on how many times a digit can be reused.
#
# You may assume the given input string is always valid.
# For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.
#
# Example 1:
#
# Input: "19:34"
# Output: "19:39"
# Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.
# It is not 19:33, because this occurs 23 hours and 59 minutes later.
#
# Example 2:
#
# Input: "23:59"
# Output: "22:22"
# Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22.
# It may be assumed that the returned time is next day's time since it is smaller than the input time numerically.

maxVals = {0:2, 1:4, 2:6, 3:9}
def nextBiggest(arr, ele, pos):
    for i, a in enumerate(arr):
        if a == ele:
            return filter(lambda x: x <= maxVals[pos], arr[i+1:])

def createTime(currTime):
    return ''.join(map(lambda x: str(x), currTime[:2])) + ':' + ''.join(map(lambda x: str(x), currTime[2:]))

def nextClosestTime(st):
    currTime = map(lambda x: int(x), list(st.replace(':', '')))
    digits = sorted(currTime)
    for i in xrange(len(currTime) - 1, -1, -1):
        ne = nextBiggest(digits, currTime[i], i)
        if len(ne) > 0:
            currTime[i] = ne[0]
            return createTime(currTime)

    #So there was no greater in the current day going the next day
    currTime = [digits[0]] * 4
    return createTime(currTime)

print nextClosestTime('23:59')
print nextClosestTime('01:34')
print nextClosestTime('12:09')
