class Solution:
    def maxDistance(self, position, m):
        position.sort()

        def can_place(dist):
            count = 1
            last = position[0]

            for i in range(1, len(position)):
                if position[i] - last >= dist:
                    count += 1
                    last = position[i]

                if count == m:
                    return True

            return False

        l = 1
        r = position[-1] - position[0]

        while l <= r:
            mid = (l + r) // 2

            if can_place(mid):
                l = mid + 1
            else:
                r = mid - 1

        return r