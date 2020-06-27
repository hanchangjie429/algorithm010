#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:     
        # https://blog.csdn.net/Mr_SCX/article/details/105456531

        # Method 1: 广度优先搜索 用队列 按层遍历树的所有节点，每遍历完一层，最大深度+1，直到最后一个叶子节点。
        '''
        if root == None: # 如果树为空，返回0
            return 0

        max_depth = 0 # 初始化最大深度为0
        queue = []
        queue.append(root)

        while queue:
            current_level_size = len(queue)
            for _ in range(current_level_size):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            max_depth += 1

        return max_depth
        '''

        # Method 2: 深度优先搜索 用栈 从根节点开始，不断往深层遍历，每遍历到一个节点，记录该节点所在深度，当遇到叶子节点时，就要考虑更新最大深度。注意：树中可能存在多个叶子节点，但只保留其中最大的深度，即最后一个叶子节点所在深度。
        '''
        if root == None:
            return 0
        stack = [(1,root),] # 初始化栈 只包括根节点 当前深度为1
        max_depth = 1

        while stack:
            depth,node = stack.pop()
            if node.left == None and node.right == None:
                max_depth = max(depth, max_depth)
            if node.left:
                stack.append((depth+1, node.left))
            if node.right:
                stack.append((depth+1, node.right))
        return max_depth
        '''    

        # Method 3: 递归 分治法，递归分别计算左子树和右子树的最大深度，并取其较大者，+1是指要算上当前节点所在的层
        '''
        if root == None:
            return 0
        return max(self.maxDepth(root.left)+1, self.maxDepth(root.right)+1)
        '''
# @lc code=end

