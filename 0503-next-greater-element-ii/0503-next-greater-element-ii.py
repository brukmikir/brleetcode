class Solution(object):

    def nextGreaterElements(self, nums):
        n = len(nums)
        ans = [-1] * n
        stack = []  # store indices

        for i in range(2 * n):
            curr = nums[i % n]

            while stack and nums[stack[-1]] < curr:
                ans[stack.pop()] = curr

            if i < n:
                stack.append(i)

        return ans