#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Method 1: 迭代 每次都新加入一个元素到所有的子集中去
        '''
        res = [[]]
        for i in nums:
            res = res+[[i]+num for num in res]
        return res
        '''
        
        # Method 2: 递归
        res = []
        def backtrack(subset, index, nums):
            if index == len(nums):
                res.append(subset)
                return 
            
            backtrack(subset, index + 1, nums)
            backtrack(subset + [nums[index]], index + 1, nums)
        backtrack([], 0, nums)
        return res

# @lc code=end

