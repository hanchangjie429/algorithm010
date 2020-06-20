#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Method 1: Brutal Method
        '''
        return sorted(s)==sorted(t)
        '''
        
        # Method 2: HashTable        
        result1 = Counter(s)
        result2 = Counter(t)
        return result1 == result2

# @lc code=end

