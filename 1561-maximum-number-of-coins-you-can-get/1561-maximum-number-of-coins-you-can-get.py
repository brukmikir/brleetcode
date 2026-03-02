class Solution(object):
    def maxCoins(self, piles):
        maxcoin=0
        piles.sort()
        m=len(piles) // 3
        i=-2
        while m > 0:
            maxcoin += piles[i]
            i -= 2
            m -= 1
        return maxcoin

        
        