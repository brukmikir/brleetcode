class Solution(object):
    def balancedString(self, s):
        n = len(s)
        cnt = {'Q':0, 'W':0, 'E':0, 'R':0}
        
        for c in s:
            cnt[c] += 1
        
        k = n // 4
        if all(cnt[c] == k for c in "QWER"):
            return 0
        
        res = n
        l = 0
        
        for r in range(n):
            cnt[s[r]] -= 1
            
            while l < n and all(cnt[c] <= k for c in "QWER"):
                res = min(res, r - l + 1)
                cnt[s[l]] += 1
                l += 1
        
        return res