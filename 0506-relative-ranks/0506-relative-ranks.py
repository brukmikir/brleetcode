class Solution(object):
    def findRelativeRanks(self, score):
        s = sorted(score, reverse=True)
        res = []

        for i in score:
            idx = s.index(i)


            if idx == 0:
                res.append("Gold Medal")
            elif idx == 1:
                res.append("Silver Medal")
            elif idx == 2:
                res.append("Bronze Medal")
            else:
                res.append(str(idx + 1))

        return res