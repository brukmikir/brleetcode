class Solution(object):
    def longestSemiRepetitiveSubstring(self, s):
        l = 0
        cnt = 0
        res = 1
        
        for r in range(1, len(s)):
            if s[r] == s[r-1]:
                cnt += 1
            
            while cnt > 1:
                if s[l] == s[l+1]:
                    cnt -= 1
                l += 1
            
            res = max(res, r - l + 1)
        
        return res