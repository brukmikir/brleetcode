class Solution(object):
    def flipAndInvertImage(self, image):
        row,col = len(image),len(image[0])

        
        for i in range(row):
            l,r = 0,col-1
            while(l <= r):
                image[i][l],image[i][r] =1-image[i][r], 1-image[i][l]
                l+=1
                r-=1                
        return image