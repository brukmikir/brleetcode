class Solution:
    def maxScore(self, cardPoints, k):
        n = len(cardPoints)
        
        total = sum(cardPoints)
        window = n - k
        
        if window == 0:
            return total
        
        curr = sum(cardPoints[:window])
        mn = curr
        
        for i in range(window, n):
            curr += cardPoints[i]
            curr -= cardPoints[i - window]
            mn = min(mn, curr)
        
        return total - mn