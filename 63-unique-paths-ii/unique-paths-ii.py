class Solution: #tc= O(m*n) sc = O(n)
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        res=0
        n=len(obstacleGrid[0])
        m=len(obstacleGrid)
        dp = [0]*n
        dp[n-1]=1
        for r in reversed(range(m)):
            for c in reversed(range(n)):
                if obstacleGrid[r][c]:
                    dp[c]=0
                elif c+1 < n:
                    dp[c] += dp [c+1]
        return dp[0]
       