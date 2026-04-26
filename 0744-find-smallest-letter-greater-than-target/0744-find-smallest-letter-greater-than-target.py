class Solution:
    def nextGreatestLetter(self, letters, target):
        l = 0
        r = len(letters)

        while l < r:
            mid = (l + r) // 2

            if letters[mid] > target:
                r = mid
            else:
                l = mid + 1

        return letters[l % len(letters)]