#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start

'''   
思路
首先判断第一个元素是不是右括号集合的，如果是，直接返回false，如果不是，将其添加入栈
然后循环整个字符串，遇到左括号，进行入栈操作，遇到右括号进行出栈操作并检查是否与栈顶元素匹配（字典）
如果不与栈顶元素匹配，直接返回false，如果匹配则继续，直到循环所有的元素，检查栈内是否有剩余元素，
如有，则返回false，没有则返回true 此处'?'为哨兵，可以省去判断栈中元素是否为空
'''

class Solution:
    def isValid(self, s):

        stck = ['?']
        dct = {'(':')','[':']','{':'}','?':'?'}
        if s == '':
            return True
        elif s[0] in dct.values():
            return False
        else:
            for i in s:
                if i in dct.keys():
                    stck.append(i)
                else:
                    if i == dct[stck[-1]]:
                        stck.pop()
                    else:
                        return False
            if stck == ['?']:
                return True
            else:
                return False

# @lc code=end

