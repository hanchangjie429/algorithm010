#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        '''
        1. 如果每一位都是9，直接返回1后面长度数量个0
        2. 如果存在有一位不是9，从最末尾开始判断当前位置是否为9，为9：当前位置修改为零并将指针前移，移动后指针位加1，直到指针指向的元素不等于0
        '''
        def all_9(digits):
            for _ in digits:
                if _ != 9:
                    return False
                else:
                    continue
            return True

        if all_9(digits):
            return [1]+[0]*len(digits)
        else:
            j = len(digits)-1
            while digits[j]+1 > 9:
                digits[j] = 0
                j -= 1
            digits[j] += 1
            return digits
# @lc code=end

