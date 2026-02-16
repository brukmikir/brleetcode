class Solution(object):
    def queryResults(self, limit, queries):
        balls={} 
        mp={}
        res=[]
        for i in queries:
            ball = i[0]
            color =i[1]
            if ball in balls:
                old=balls[ball]
                mp[old] -= 1
                if (mp[old] == 0):
                    del mp[old]


            balls[ball] = color
            if color in mp:
                mp[color] += 1
            else:
                mp[color] = 1

            res.append(len(mp))
        return res

        
        