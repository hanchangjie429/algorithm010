#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights):
        # Method 1: Brutal Method
        '''
        size = len(heights)
        res = 0
        for i in range(size):
            cur_height = heights[i]
            l = i
            while l > 0 and heights[l-1] >= cur_height:
                l -= 1
            r = i
            while r < size - 1 and heights[r+1] >= cur_height:
                r += 1
            max_width = r - l + 1
            res = max(res, max_width*cur_height)
        return res
        '''

        # Method 2: Using Stack
        heights = [0] + heights + [0]
        size = len(heights)
        stck = [0]
        res = 0

        for i in range(1,size):
            while heights[i] < heights[stck[-1]]:
                height = heights[stck.pop()]
                max_width = i - stck[-1] - 1
                area = height * max_width
                res = max(res,area)
            stck.append(i)
        return res
# @lc code=end

