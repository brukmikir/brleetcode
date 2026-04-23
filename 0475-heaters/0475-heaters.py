class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        max_radius = 0
        n = len(heaters)
        
        for house in houses:
            low = 0
            high = n - 1
            
            while low <= high:
                mid = (low + high) // 2
                if heaters[mid] < house:
                    low = mid + 1
                else:
                    high = mid - 1
            
            dist_right = heaters[low] - house if low < n else float('inf')
            dist_left = house - heaters[low - 1] if low > 0 else float('inf')
            
            current_min_dist = min(dist_left, dist_right)
            
            if current_min_dist > max_radius:
                max_radius = current_min_dist
                
        return max_radius