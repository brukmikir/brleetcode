class Solution(object):
    def majorityElement(self, nums):
        n = len(nums)
        ratio = n // 3
        nums.sort()
        res = []

        i = 0
        while i < n:
            count = 1
            while i + 1 < n and nums[i] == nums[i + 1]:
                count += 1
                i += 1

            if count > ratio:
                res.append(nums[i])

            i += 1

        return res


            
                

        
        