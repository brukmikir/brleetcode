class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        points.sort()
        res=0

        for i in range(len(points)-1):
            res=max(res,abs(points[i][0]-points[i+1][0]))
        return res

        

       

        
        