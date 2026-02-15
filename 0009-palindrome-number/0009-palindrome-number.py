class Solution(object):
    def isPalindrome(self, x):
        y=str(x)
        left,right = 0, len(y)-1

        while left < right:
            if y[left] != y[right]:
                return False
            left += 1
            right -= 1
        return True   
        
        

        