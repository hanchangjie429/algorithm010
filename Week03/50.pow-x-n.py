#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Method 1: 直接用公式
        '''
        return pow(x,n)
        '''

        # Method 2: 暴力循环法
        # 处理n为负数的情况，也就是将x转换成1/x，然后不断乘1/x
        '''
        if n < 0:
            x = 1/x
            n = -n
        ans = 1
        for _ in range(n):
            ans *= x
        return ans
        '''

        # Method 3 递归 二分法
        #https://leetcode-cn.com/problems/powx-n/solution/powx-n-by-leetcode-solution/
        def divide(x, n):
            if n == 1:
                return x
            if n%2 != 0:
                half = divide(x, n//2)
                return half * half * x
            else:
                half = divide(x, n//2)
                return half * half

        if n==0 or x == 1:
            return 1
        if n < 0:
            return 1/divide(x,-n)
        return divide(x,n)

# @lc code=end

