from collections import deque

class Solution(object):
    def longestSubarray(self, nums, limit):
        maxd = deque()
        mind = deque()
        
        l = 0
        ans = 0
        
        for r in range(len(nums)):
            while maxd and nums[maxd[-1]] < nums[r]:
                maxd.pop()
            maxd.append(r)
            
            while mind and nums[mind[-1]] > nums[r]:
                mind.pop()
            mind.append(r)
            
            while nums[maxd[0]] - nums[mind[0]] > limit:
                if maxd[0] == l:
                    maxd.popleft()
                if mind[0] == l:
                    mind.popleft()
                l += 1
            
            ans = max(ans, r - l + 1)
        
        return ans