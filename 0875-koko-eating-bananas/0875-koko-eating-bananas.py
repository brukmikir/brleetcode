class Solution:
    def minEatingSpeed(self, piles, h):
        
        def canEat(speed):
            hours = 0
            for p in piles:
                hours += (p + speed - 1) // speed
            return hours <= h
        
        left, right = 1, max(piles)
        answer = right
        
        while left <= right:
            mid = (left + right) // 2
            
            if canEat(mid):
                answer = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return answer