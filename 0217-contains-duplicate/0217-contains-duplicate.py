class Solution(object):
    def containsDuplicate(self, nums):
        setnum= set(nums)
        return len(nums)> len(setnum)
        