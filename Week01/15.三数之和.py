#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums):
        '''method 1 暴力法 时间复杂度太高
        lst = []
        nums = sorted(nums)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[i]+ nums[j]+nums[k] == 0 and [nums[i],nums[j],nums[k]] not in lst:#要保证没有重复的元素
                        lst.append([nums[i],nums[j],nums[k]])
        return lst
        '''

        '''method 2 两次循环＋hashmap 有待补充！！！
        
        .......
        '''

        '''method 3 双指针
        1st step: sort the whole list
        2nd step: loop the whole list with k and create 2 pointer i and j, one(i) from left to right (ascend) 
        one(j) from right to left (descend)
        3rd step: fix k and move i and j to find the result that satisfy the condition
        4th step: move k and loop 3rd step untill k==len(nums)-3
        '''
        nums = sorted(nums)
        res = []
        for k in range(len(nums)-2):
            if nums[k] > 0:
                break
            if k > 0 and nums[k] == nums[k-1]:
                continue
            i = k + 1
            j = len(nums) - 1
            while i < j:
                sum = nums[k]+nums[i]+nums[j]
                if sum < 0:
                    i += 1
#                    while i < j and nums[i] == nums[i-1]:
#                        i += 1
                elif sum > 0:
                    j -= 1
#                    while i < j and nums[j] == nums[j+1]:
#                        j -= 1
                else:
                    res.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i-1]:
                        i += 1
                    while i < j and nums[j] == nums[j+1]:
                        j -= 1
        return res


# @lc code=end
