class Solution:
    def shipWithinDays(self, weights, days):
        left = max(weights)
        right = sum(weights)

        while left <= right:
            mid = (left + right) // 2

            need = 1
            cur = 0

            for w in weights:
                if cur + w <= mid:
                    cur += w
                else:
                    need += 1
                    cur = w

            if need <= days:
                right = mid - 1
            else:
                left = mid + 1

        return left