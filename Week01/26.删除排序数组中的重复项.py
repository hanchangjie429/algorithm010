#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Method 1 loop
        '''
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums.pop(i)# 问题出现在，pop数组的元素后，整个数组的index都发生了变化
            else:
                pass
        return len(nums)
        '''
        # 如果只是找到移除后新数组的长度可以用count计数
        '''
        count = 1
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                count += 1
            else:
                pass
        return count
        '''
        # 更新 刚刚看到题解有人说，题目中明确说到“你不需要考虑数组中超出新长度后面的元素”，意思就是根本不需要删除数组中的元素。。。还是题意没弄清楚啊。。。
        # 这里使用快慢指针来解决，慢指针指向递增的元素，快指针遍历整个数组
        i = 0
        for j in range(len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
            else:
                pass
        return i + 1
# @lc code=end

