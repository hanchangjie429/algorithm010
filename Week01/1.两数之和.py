#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums, target):
        '''method 1    暴力解法
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
                else:
                    pass
        '''

        '''method 2 建立一个hashmap用于查询 两次hash
        ''' 
        hashmap = {}
        for index, item in enumerate(nums):
            hashmap[target - item] = index
        
        for index, item in enumerate(nums):
            if item in hashmap and index != hashmap[item]:
                return [index, hashmap[item]]

        '''method 3 网友改进method 2 一次hash
        dct = {}
        for i, n in enumerate(nums):
            if target - n in dct:
                return [dct[target - n], i]
            dct[n] = i
        '''

# @lc code=end


