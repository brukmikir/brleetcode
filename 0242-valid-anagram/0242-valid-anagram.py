class Solution(object):
    def isAnagram(self, s, t):
        sorteds=sorted(s)
        sortedt=sorted(t)

        return sorteds == sortedt
       
        
        