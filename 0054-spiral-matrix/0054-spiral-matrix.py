class Solution:
    def spiralOrder(self, mat: list[list[int]]) -> list[int]:
        m,n=len(mat),len(mat[0])
        left,right=0,n-1
        top,bottom=0,m-1
        res=[]
        while top<=bottom and left<=right:
            for i in range(left,right+1):
                res.append(mat[top][i])
            top+=1
            for i in range(top,bottom+1):
                res.append(mat[i][right])
            right-=1
            if(top<=bottom):
                for i in range(right,left-1,-1):
                    res.append(mat[bottom][i])
                bottom-=1
            if(left<=right):
                for i in range(bottom,top-1,-1):
                    res.append(mat[i][left])
                left+=1
        return res
                
