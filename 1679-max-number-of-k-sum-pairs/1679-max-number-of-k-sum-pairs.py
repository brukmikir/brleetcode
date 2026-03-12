class Solution(object):
    def maxOperations(self, nums, k):
        l=0
        r=len(nums)-1
        nums.sort()
        count=0

        while l<r:
            if(nums[l] + nums[r]) < k:
                l+=1
            elif(nums[l] + nums[r]) > k:
                r-=1
            else:
                l+=1
                r-=1
                count+=1
        return count


        
        