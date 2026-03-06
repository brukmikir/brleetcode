class Solution(object):
    def reductionOperations(self, nums):
        nums.sort()
        
        count = 0
        steps = 0
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                steps += 1
            count += steps
        
        return count
        