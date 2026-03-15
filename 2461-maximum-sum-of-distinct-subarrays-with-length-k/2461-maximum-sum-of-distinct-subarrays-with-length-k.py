from collections import defaultdict

class Solution:
    def maximumSubarraySum(self, nums, k):
        freq = defaultdict(int)
        window_sum = 0
        ans = 0
        left = 0

        for right in range(len(nums)):
            freq[nums[right]] += 1
            window_sum += nums[right]

            if right - left + 1 > k:
                freq[nums[left]] -= 1
                window_sum -= nums[left]
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1

            if right - left + 1 == k and len(freq) == k:
                ans = max(ans, window_sum)

        return ans