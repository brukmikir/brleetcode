class Solution(object):
    def matrixSum(self, nums):
        score = 0
        
        while nums[0]:
            removed = []
            
            for row in nums:
                m = max(row)
                row.remove(m)
                removed.append(m)
            
            score += max(removed)
        
        return score

                
                
        
         
        