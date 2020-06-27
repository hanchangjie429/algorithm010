#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Method 1 Hashmap
        '''
        dict = {}
        for i in nums:
            if i not in dict:
                dict[i] = 0
            else:
                dict[i] += 1
        return max(dict, key = dict.get)
        '''

        
# @lc code=end

