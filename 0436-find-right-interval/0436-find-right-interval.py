class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        starts = []
        for i in range(n):
            starts.append([intervals[i][0], i])
        
        starts.sort()
        result = []
        
        for i in range(n):
            target = intervals[i][1]
            
            low = 0
            high = n - 1
            ans = -1
            
            while low <= high:
                mid = (low + high) // 2
                if starts[mid][0] >= target:
                    ans = starts[mid][1]
                    high = mid - 1
                else:
                    low = mid + 1
            
            result.append(ans)
            
        return result