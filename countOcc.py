class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def PosBinarySearch(self, left, right, arr, x, first=True):
        if left + 1 >= right:
            print 'HI', first
            if first:
                return left if arr[left] >= x else left + 1 if 
            else:
                print right, left
                return right if arr[right] > x else right + 1
        mid = (left + right)//2
        if first:
            if arr[mid] >= x:
                return self.PosBinarySearch(left, mid, arr, x, first)
            else:
                return self.PosBinarySearch(mid + 1, right, arr, x, first)
        else:
            if arr[mid] > x:
                return self.PosBinarySearch(left, mid-1, arr, x, first)
            return self.PosBinarySearch(mid, right, arr, x, first)
            
        
        
    def findCount(self, A, B):
        firstInd = self.PosBinarySearch(0, len(A)-1, A, B)
        LastInd = self.PosBinarySearch(0, len(A)-1, A, B, False)
        print firstInd, LastInd, 1
        return LastInd - firstInd + 1


obj = Solution()
A = [ 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 7, 7, 8, 8, 8, 8, 9, 9, 10, 10, 10 ]
B = 1
print obj.findCount(A, B)
