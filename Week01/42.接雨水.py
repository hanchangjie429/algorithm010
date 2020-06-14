#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        # Method 1: calculate by row
        sum = 0
        max_height = max(height)
        for i in range(max_height):
            isStart = False
            temp_sum = 0
            for j in range(len(height)):
                if isStart and height[j]<i:
                    temp_sum += 1
                if height[j]>=i:
                    sum += temp_sum
                    temp_sum = 0
                    isStart = True
        return sum

# @lc code=end

