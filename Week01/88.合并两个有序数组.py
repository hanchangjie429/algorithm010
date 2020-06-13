#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Method 1: 2 pointer from the start
        '''
        nums1_copy = nums1[:m]
        nums1[:] = [] #注意list[:] 和 list 的区别

        i = 0
        j = 0

        while i < m and j < n:
            if nums1_copy[i]< nums2[j]:
                nums1.append(nums1_copy[i])
                i += 1
            else:
                nums1.append(nums2[j])
                j += 1
        if i < m:
            nums1[i+j:] = nums1_copy[i:]
        if j < n:
            nums1[i+j:] = nums2[j:]
        '''

        # Method 2: Pointer from the end
        p1 = m-1
        p2 = n-1

        p = m+n-1  # 所以是从M+n-1开始放数字，而不是从nums1 的最后开始
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] < nums2[p2]:
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                nums1[p] = nums1[p1]
                p1 -= 1
            p -= 1

        nums1[:p2+1] = nums2[:p2+1]
        #如果p1指针遍历完成了但p2指针还没遍历完，此时应该继续遍历p2指针并填入p指针，由于p2是有序的，就直接用复制数组代替了遍历写入。 如果p2指针遍历完了但p1指针还没遍历完，此时应该继续遍历p1并填入p指针，但由于此时p1指针和p指针重合，所以可以省略遍历操作。

# @lc code=end

