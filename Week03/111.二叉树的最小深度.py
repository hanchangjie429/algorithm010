#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        # https://blog.csdn.net/Mr_SCX/article/details/105456531
        # Method 1: 广度优先搜索 按层遍历整颗二叉树，只要找到第一个叶子节点，其深度即为最小深度。
        '''
        if root == None:
            return 0
        min_depth = 0 # 如果存在根节点 最小深度初始化为1
        queue = []
        queue.append(root) # 加入根节点

        while queue:
            min_depth += 1 # 只要队列不为空，说明当前遍历到的这一层有节点，min_depth+1
            current_depth_size = len(queue)
            for _ in range(current_depth_size): # 遍历当前层的每个节点
                node = queue.pop(0)
                if node.left == None and node.right == None: # 只要找到第一个叶子节点，该节点所在层就是最小深度
                    return min_depth
                # 若当前节点存在孩子节点，将孩子节点入队
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
        return min_depth
        '''

        # Method 2 深度优先搜索 深度优先搜索一般是借助栈来实现。从根节点开始，不断往深层遍历，每遍历到一个节点，记录该节点所在深度，当遇到叶子节点时，就要考虑更新最小深度。注意：树中可能存在多个叶子节点，但只保留其中最小的深度，即第一个叶子节点所在深度。
        '''
        if root == None:
            return 0
        stack = [(1, root),] # 栈中初始只包含根节点，当前深度为1
        min_depth = float('inf') # min_depth初始化为无穷大

        while stack:
            depth, node = stack.pop()
            if node.left == None and node.right == None: # 遇到当前节点为叶子节点时，更新最小深度
                min_depth = min(depth, min_depth) # 只保留其中最小的深度
            if node.left: # 若存在左孩子，则压入栈，深度+1
                stack.append((depth+1, node.left))
            if node.right:  # 若存在右孩子，则压入栈，深度+1
                stack.append((depth+1, node.right))
        
        return min_depth
        ''' 

        # Method 3 分治法
        '''
        if root == None:
            return 0
        if root.left == None and root.right != None:
            return 1 + self.minDepth(root.right)
        if root.right == None and root.left != None:
            return 1 + self.minDepth(root.left)
        return 1 + min(self.minDepth(root.left),self.minDepth(root.right)) 
        '''
# @lc code=end

