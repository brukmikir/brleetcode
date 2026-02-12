class Solution(object):
    def uniqueMorseRepresentations(self, words):
        transformer=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        res=[]
        for i in words:
            cur=[]
            for j in i:
                j.lower()
                cur.append(transformer[ord(j)-97])
            res.append("".join(cur))
        result=set(res)
        return len(result)
        
        