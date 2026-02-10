class Solution(object):
    def findDuplicates(self, nums):
        res=[]
        nums.sort()

        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                res.append(nums[i])
        return res
        