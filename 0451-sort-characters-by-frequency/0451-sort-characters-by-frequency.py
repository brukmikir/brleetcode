class Solution(object):
    def frequencySort(self, s):
        freqn = {}

        for c in s:
            if c in freqn:
                freqn[c] += 1
            else:
                freqn[c] = 1

        sorted_chars = sorted(freqn, key=freqn.get, reverse=True)

        res = ""
        for c in sorted_chars:
            res += c * freqn[c]

        return res

        