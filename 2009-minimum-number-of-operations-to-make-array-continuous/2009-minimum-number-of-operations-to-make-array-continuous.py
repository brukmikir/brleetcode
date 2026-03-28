class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        unique_nums = sorted(set(nums))
        
        max_elements_in_window = 0
        j = 0
        m = len(unique_nums)
        
        for i in range(m):
            while j < m and unique_nums[j] <= unique_nums[i] + n - 1:
                j += 1
            
            max_elements_in_window = max(max_elements_in_window, j - i)
            
        return n - max_elements_in_window
        