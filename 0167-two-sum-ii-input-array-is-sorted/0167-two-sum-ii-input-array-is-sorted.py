class Solution(object):
    def twoSum(self, numbers, target):
        l=0
        r=len(numbers)-1
        res=[]

        while l<r:
            nm=numbers[l] + numbers[r]
            if ( nm == target):
                return [l+1,r+1]
            elif(nm < target):
                l+=1
            else:
                r-=1
        return res


        
        