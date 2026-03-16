class Solution:
    def minimumRecolors(self, blocks, k):
        w = 0
        
        for i in range(k):
            if blocks[i] == 'W':
                w += 1
        
        ans = w
        
        for i in range(k, len(blocks)):
            if blocks[i - k] == 'W':
                w -= 1
            if blocks[i] == 'W':
                w += 1
            
            ans = min(ans, w)
        
        return ans