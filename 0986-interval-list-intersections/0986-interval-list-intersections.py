class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        i = 0
        j = 0
        res = []

        while i < len(firstList) and j < len(secondList):
            a, b = firstList[i]
            c, d = secondList[j]

            start = max(a, c)
            end = min(b, d)

            if start <= end:
                res.append([start, end])

            if b < d:
                i += 1
            else:
                j += 1

        return res