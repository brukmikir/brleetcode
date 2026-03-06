class Solution(object):
    def appendCharacters(self, s, t):
        samepre = 0
        j = 0
        
        for i in range(len(s)):
            if j < len(t) and s[i] == t[j]:
                samepre += 1
                j += 1
                
        return len(t) - samepre