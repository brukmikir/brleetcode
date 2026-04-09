class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        nge = {}

        for num in nums2:
            while stack and num > stack[-1]:
                top = stack.pop()
                nge[top] = num
            stack.append(num)

        res = []

        for x in nums1:
            if x in nge:
                res.append(nge[x])
            else:
                res.append(-1)

        return res