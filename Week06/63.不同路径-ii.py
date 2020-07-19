#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # 特殊情况
        if obstacleGrid == None:
            return 0
        m = len(obstacleGrid) # hangshu
        n = len(obstacleGrid[0]) # lieshu

        if obstacleGrid[0][0] == 1:
            return 0

        # 初始化
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = 1

        # 第一行和第一列
        for i in range(1,m):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = dp[i-1][0]
        for j in range(1,n):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = dp[0][j-1]
                
        # dp过程
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]




# @lc code=end

