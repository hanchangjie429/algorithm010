#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hashmap = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def recursive(letters,index,digits):
            if index == len(digits):
                res.append(letters)
                return

            for i in hashmap[digits[index]]:
                recursive(letters + i, index + 1, digits)
        # 特殊情况        
        if digits == '':
            return []
        res = []
        recursive('', 0, digits)
        return res
# @lc code=end

