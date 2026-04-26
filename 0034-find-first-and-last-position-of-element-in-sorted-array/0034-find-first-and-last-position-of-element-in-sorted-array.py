class Solution(object):
    def searchRange(self, nums, target):
        if target not in nums:
            return [-1,-1]
        for i in range(len(nums)):
            if nums[i]==target:
                l=i
        return [nums.index(target),l]
        