class Solution(object):
    def removeDuplicates(self, nums):
        l=0
        r=1
        while r<len(nums):
            if nums[l]==nums[r]:
                nums.remove(nums[r])
            else:
                l+=1
                r+=1
            
            
        return len(nums)
        
        