class Solution(object):
    def numberOfSubarrays(self, nums, k):

        def atMost(k):
            l = 0
            count = 0
            ans = 0

            for r in range(len(nums)):
                if nums[r] % 2:
                    count += 1

                while count > k:
                    if nums[l] % 2:
                        count -= 1
                    l += 1

                ans += r - l + 1

            return ans

        return atMost(k) - atMost(k-1)