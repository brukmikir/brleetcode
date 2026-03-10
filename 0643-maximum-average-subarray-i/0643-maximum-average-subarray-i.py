class Solution(object):
    def findMaxAverage(self, nums, k):
        l = 0
        r = k
        s = 0

        for i in range(k):
            s += nums[i]

        ans = s

        while r < len(nums):
            s -= nums[l]
            s += nums[r]
            ans = max(ans, s)
            l += 1
            r += 1

        return float(ans) / k
            

                
        