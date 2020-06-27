#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # 递归函数的终止条件，节点为空时返回
        '''
        if root == None:
            return None
        # 将当前节点的左右子树交换
        root.left, root.right = root.right, root.left
        # 递归交换当前节点的 左子树和右子树
        self.invertTree(root.left)
        self.invertTree(root.right)
        # 函数返回时就表示当前这个节点，以及它的左右子树
		# 都已经交换完了
        return root
        '''
        
        # 迭代方法 我们需要交换树中所有节点的左孩子和右孩子， 因此可以创建一个队列来存储所有左孩子和右孩子还没有被交换过的节点

        if root == None:
            return None
        queue = deque()
        queue.append(root)

        while queue:
            current = queue.pop()
            current.left, current.right = current.right, current.left
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)
        
        return root
# @lc code=end

