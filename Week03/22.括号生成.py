#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Method 1: backtrack
        '''
        https://leetcode-cn.com/problems/generate-parentheses/solution/hui-su-suan-fa-by-liweiwei1419/
        '''
        '''
        res = []
        def backtrack(s, left, right):
            # 如果左右括号都用完，结束递归
            if len(s) == 2*n:
                res.append(s)
                return
            # 如果左括号小于n，可以继续添加左括号
            if left < n:
                backtrack(s+'(',left+1,right)
            # 如果右括号小于左括号，可以继续添加右括号
            if right < left:
                backtrack(s+')',left,right+1)
        backtrack('',0,0)
        return res
        '''

        #递减序列
        res = []
        def dfs(str, left, right):
            if left == 0 and right == 0:
                res.append(str)
                return
            if left > 0:
                dfs(str+'(',left - 1, right)
            if right > left:
                dfs(str+')',left, right - 1)
        dfs('',n,n)
        return res

    '''
        # 思路 需要一个res储存每一个可能的结果 需要一个递归函数
        def recursive(string, left=0, right=0):
            # 默认left right为零, 因为还没开始添加
            # 退出条件 左右括号都满了即left==n and right==n，此时可以输出结果，即append（result）
            # 1. 什么时候可以加左括号 当左括号还有剩余，随时可以加左括号
            # 2. 什么时候可以加右括号，当用过的左括号剩余严格大于右括号，时，随时可以加右括号
            if left == n and right == n:
                res.append(string)
                return
            if left < n:
                recursive(string+'(',left+1,right)
            if left > right:
                recursive(string+')',left, right+1)
        res = []
        recursive('')
        return res
        '''
# @lc code=end

