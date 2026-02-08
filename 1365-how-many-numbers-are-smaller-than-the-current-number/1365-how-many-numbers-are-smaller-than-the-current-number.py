class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        sorted_nums = sorted(nums)
        index_map = {}

        for i, num in enumerate(sorted_nums):
            if num not in index_map:
                index_map[num] = i

        return [index_map[num] for num in nums]

        