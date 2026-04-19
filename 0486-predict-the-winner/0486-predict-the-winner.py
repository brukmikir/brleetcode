class Solution:
    def predictTheWinner(self, nums):
        n = len(nums)
        dp = [[None] * n for _ in range(n)]
        
        def dfs(l, r):
            if l == r:
                return nums[l]
            
            if dp[l][r] is not None:
                return dp[l][r]
            
            dp[l][r] = max(
                nums[l] - dfs(l + 1, r),
                nums[r] - dfs(l, r - 1)
            )
            
            return dp[l][r]
        
        return dfs(0, n - 1) >= 0