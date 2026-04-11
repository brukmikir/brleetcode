class Solution:
    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0
        
        for i in range(len(heights) + 1):
            cur = heights[i] if i < len(heights) else 0
            
            while stack and heights[stack[-1]] > cur:
                h = heights[stack.pop()]
                
                if not stack:
                    width = i
                else:
                    width = i - stack[-1] - 1
                
                max_area = max(max_area, h * width)
            
            stack.append(i)
        
        return max_area