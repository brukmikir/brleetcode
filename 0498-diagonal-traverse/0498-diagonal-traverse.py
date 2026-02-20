class Solution(object):
    def findDiagonalOrder(self, mat):
        row=len(mat)
        col=len(mat[0])

        res=[]

        cur_row,cur_col =0,0
        goup=True

        while(len(res) < row * col):
            if goup:
                while(cur_row >= 0 and cur_col < col):
                    res.append(mat[cur_row][cur_col])

                    cur_row-=1
                    cur_col+=1
                
                if cur_col == col:
                    cur_col-=1
                    cur_row+=2
                else:
                    cur_row += 1
                goup=False
            else:

                while(cur_row < row and cur_col >= 0):
                    res.append(mat[cur_row][cur_col])

                    cur_row += 1
                    cur_col -= 1
                
                if cur_row == row:
                    cur_row -= 1
                    cur_col += 2
                else:
                    cur_col += 1
                goup=True
        return res




        
        
        
        