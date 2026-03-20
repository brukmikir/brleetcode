class Solution(object):
    def getAverages(self, nums, k):
        n = len(nums)
        res = [-1] * n
        
        if k == 0:
            return nums
        
        window = 2 * k + 1
        if window > n:
            return res
        
        s = sum(nums[:window])
        res[k] = s // window
        
        for i in range(window, n):
            s += nums[i]
            s -= nums[i - window]
            res[i - k] = s // window
        
        return res