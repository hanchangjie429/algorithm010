#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x):
        if x < 0:
            x = -x
		    x = '-'+str(x)[::-1]
            return int(x)
	    else:
		    x = str(x)[::-1]
            return int(x)
        

# @lc code=end

