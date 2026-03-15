from collections import Counter

class Solution(object):
    def findAnagrams(self, s, p):
        res = []
        k = len(p)

        countP = Counter(p)
        window = Counter()

        l = 0
        for r in range(len(s)):
            window[s[r]] += 1

            if r - l + 1 > k:
                window[s[l]] -= 1
                if window[s[l]] == 0:
                    del window[s[l]]
                l += 1

            if window == countP:
                res.append(l)

        return res