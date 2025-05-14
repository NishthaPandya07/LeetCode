class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        final=[[0]* n for _ in range(n)]
        left,top=0,0
        bottom,right=n,n
        counter=1
        while left<=right: #or top<=bottom (because it is square matrix)
            for i in range(left,right):
                final[top][i]=counter
                counter+=1
            top+=1
            for i in range(top,bottom):
                final[i][right-1]=counter
                counter+=1
            right-=1
            if left > right or top > bottom:
                break
            for i in range(right,left,-1):
                final[bottom-1][i-1]=counter
                counter+=1
            bottom-=1
            for i in range(bottom,top,-1):
                final[i-1][left]=counter
                counter+=1
            left+=1
        return final
        