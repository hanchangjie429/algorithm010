#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # Method 1: 回溯法
        def backtrack(first = 1, curr = []):
            if len(curr) == k:
                res.append(curr[:])
                return 
            for i in range(first, n+1):
                curr.append(i)
                backtrack(i+1, curr)
                curr.pop()
        res = []
        backtrack()
        return res
# @lc code=end

