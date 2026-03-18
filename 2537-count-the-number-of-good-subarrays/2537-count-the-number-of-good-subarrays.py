class Solution:
    def countGood(self, nums, k):
        count = {}
        left = 0
        pairs = 0
        res = 0
        
        for right in range(len(nums)):
            num = nums[right]
            
            if num in count:
                pairs += count[num]
                count[num] += 1
            else:
                count[num] = 1
            
            while pairs >= k:
                res += len(nums) - right
                
                left_num = nums[left]
                count[left_num] -= 1
                pairs -= count[left_num]
                left += 1
        
        return res
        