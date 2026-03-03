class Solution(object):
    def moveZeroes(self, nums):
        hol=0
        sik=0

        while sik < len(nums):
            if nums[sik] != 0:
                nums[hol],nums[sik] = nums[sik],nums[hol]
                sik+=1
                hol+=1
            else:
                sik+=1
        return nums
        
        