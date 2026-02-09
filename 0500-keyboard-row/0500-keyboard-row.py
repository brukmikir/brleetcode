class Solution(object):
    def findWords(self, words):
        row1="qwertyuiop"
        row2="asdfghjkl"
        row3="zxcvbnm"

        res=[]

        for i in words:
            I=i.lower()

            if all(char in row1 for char in I ):
                res.append(i)
            if all(char in row2 for char in I):
                res.append(i)
            if all(char in row3 for char in I ):
                res.append(i)
        return res
            
                

        