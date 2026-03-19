class Solution(object):
    def maxTurbulenceSize(self, arr):
        n = len(arr)
        if n == 1:
            return 1
        
        res = 1
        l = 0
        
        def cmp(a, b):
            if a > b: return 1
            if a < b: return -1
            return 0
        
        for r in range(1, n):
            c = cmp(arr[r-1], arr[r])
            
            if c == 0:
                l = r
            elif r == n-1 or c * cmp(arr[r], arr[r+1]) != -1:
                res = max(res, r - l + 1)
                l = r
        
        return res