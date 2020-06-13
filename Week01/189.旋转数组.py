#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 旋转数组
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Method 1: Brutal Method
        '''
        for _ in range(k):#控制旋转次数
            previous = nums[len(nums)-1]
            for j in range(len(nums)):#旋转整个数组
                nums[j],previous = previous, nums[j]
        '''        
        # Method 2: Create an extra list, put index:i -> index:(i+k)%length
        '''
        newlst = [0]*(len(nums))
        for i in range(len(nums)):
            newlst[(i+k)%len(nums)] = nums[i]
        for i in range(len(nums)):
            nums[i] = newlst[i]
        '''

        # Method 3: Reverse
        
        def reverse(nums,start,end):
            while start < end:
                nums[start],nums[end] = nums[end],nums[start]
                start += 1
                end -= 1
        
        k %= len(nums)
        reverse(nums,0,len(nums)-1)
        reverse(nums,0,k-1)
        reverse(nums,k,len(nums)-1)
        
# @lc code=end

