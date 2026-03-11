class Solution(object):
    def maxArea(self, height):
        maxa=0;
        l=0;
        r=len(height)-1;
        for i in range(len(height)):
                area= abs(l-r)*min(height[r],height[l]);
                   
                if(area>maxa):
                      maxa=area;
                   

                if(height[l]>height[r]):
                    r-=1
                else:
                    l+=1

        return maxa;