#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums ,k):
        # Method 1: Brutal Method
        '''
        return [max(nums[i:i+k]) for i in range(len(nums)-k+1)]
        '''

        # Method 2: Using Deque
        from collections import deque
        if len(nums)*k == 0:
             return []
        elif k == 1:
            return nums
        else:
            deq = deque()
            res = []
            for i in range(len(nums)):
                left = i - k + 1
                right = i
                while deq and nums[i] > nums[deq[-1]]:
                    deq.pop()
                deq.append(i)
                if left <= deq[0] <= right:
                    res.append(nums[deq[0]])
                else:
                    deq.popleft()
                    res.append(nums[deq[0]])
            return res[k-1:]

# @lc code=end

