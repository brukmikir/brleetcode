class Solution(object):
    def checkSubarraySum(self, nums, k):
        
        remander={0:-1} 
        total=0

        for i,n in enumerate(nums):
            total += n
            r=total % k
            if r not in remander:
                remander[r] = i
            elif i-remander[r] > 1:
                return True
        return False

        