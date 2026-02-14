class Solution(object):
    def flipAndInvertImage(self, image):
        row,col = len(image),len(image[0])

        
        for i in range(row):
            l,r = 0,col-1
            while(l < r):
                image[i][l],image[i][r] = image[i][r],image[i][l]
                l+=1
                r-=1
        for r in range(row):
            for c in range(col):
                if image[r][c] == 0:
                    image[r][c]+=1
                elif image[r][c] == 1:
                    image[r][c]-=1
        return image