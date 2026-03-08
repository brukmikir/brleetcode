class Solution(object):
    def thirdMax(self, nums):
        setnk=set(nums)
        setn = sorted(setnk)
        if len(setn)<3:
            return setn[-1]
        else:
            return setn[-3] 
        
        