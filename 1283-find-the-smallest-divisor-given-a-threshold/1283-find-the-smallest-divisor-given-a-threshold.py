class Solution:
    def smallestDivisor(self, nums, threshold):
        def compute(d):
            total = 0
            for x in nums:
                total += (x + d - 1) // d
            return total

        left, right = 1, max(nums)

        while left < right:
            mid = (left + right) // 2
            if compute(mid) <= threshold:
                right = mid
            else:
                left = mid + 1

        return left