#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n):
        '''找最近重复子问题 递归就是从f(n)出发，往前递推，寻找f(n-1),f(n-2),直到f(2),f(1)，然后往回迭代...，但是循环则是从f(1),f(2)开始，
        顺序往后计算，直到到达退出循环的点。递归复杂度为O(2^n),而循环的复杂度为O(n)'''
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
# @lc code=end

