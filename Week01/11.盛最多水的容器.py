#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height):
        '''
        方法一：枚举出所有的容器容量，然后再比较大小(超出时间限制)
        max_area = 0
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                area = (j - i) * min(height[i], height[j])
                max_area = max(max_area, area)
        return max_area
        '''

        '''
        方法二：从两边向中间收敛
        i,j
        max_area = 0
        i++, j--
        判断是i+还是j-，就是判断height[i]和height[j]谁比较小，谁小挪谁，计算此时的面积并和当前最大面积比较,更新最大面积
        直到i和j相等，i==j，退出循环，输出最大面积
        '''
        i = 0
        j = len(height)-1
        max_area = (j-i) * min(height[i],height[j])
        while i != j:
            if height[i]<=height[j]:
                i += 1
                area = (j-i) * min(height[i],height[j])
            else:
                j -= 1
                area = (j-i) * min(height[i],height[j])
            max_area = max(max_area,area)
        return max_area
# @lc code=end

