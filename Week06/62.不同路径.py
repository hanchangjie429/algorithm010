#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#

'''
解题思路：
1. 确定状态方程
我们使用一个二维数组dp来储存答案，dp[i][j]表示从起始点dp[0][0]走到当前点(i,j)的路径数

2. 确定状态转移方程
因为每一个点只能从上面一个点往下走一步，或者从左边一个点往右走一步，因此状态转移方程为dp[i][j] = dp[i-1][j] + dp[i][j-1]

3.确定边界条件
第一行和第一列因为只能往右走和只能往下走，因此在这两列上的元素的走法统统为1，然后从dp[1][1]开始，到达每一个格子的走法都可以通过状态转移方程求出来，最终将dp二维数组填满，而我们要的答案就在dp的最后一个位置，也就是dp[n-1][m-1]
'''


# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 初始化dp，确定边界条件
        dp = [[1]*m]+[[1]+[0]*(m-1) for _ in range(n-1)]
        # 状态转移方程
        for i in range(1,n):
            for j in range(1,m):
                dp[i][j] = dp[i-1][j]+dp[i][j-1]
        
        return dp[-1][-1]
# @lc code=end

