#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n):
        # Method 1: 递归方法 (会超时) 时间复杂度O(2^n) 空间复杂度O(1)
        '''
        if n <= 1:
            return 1
        elif n < 3:
            return n
        else:
            return self.climbStairs(n-1)+self.climbStairs(n-2)
        '''

        # Method 2: Dynamic Programming 时间复杂度O(n) 空间复杂度O(n)
        '''
        dp = {}
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n]
        '''
        
        # Method 3: 循环方法
        '''找最近重复子问题 递归就是从f(n)出发，往前递推，寻找f(n-1),f(n-2),直到f(2),f(1)，然后往回迭代...，但是循环则是从f(1),f(2)开始，
        顺序往后计算，直到到达退出循环的点。递归复杂度为O(2^n),而循环的时间复杂度为O(n) 空间复杂度O(1)'''
        '''
        a1 = 1
        a2 = 2
        a3 = 3
        if n <= 2:
            return n
        for _ in range(3,n+1):
            a3 = a1 + a2
            a1 = a2
            a2 = a3
        return a3
        '''

        # Method 4: 网上看到一个超级简洁的答案
        if n < 3: return n
        a, b = 1, 2
        for _ in range(3,n+1):
            a,b = b,a + b
        return b


# @lc code=end

