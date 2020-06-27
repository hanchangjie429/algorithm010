#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # Method 1: 递归 如果该二叉树的左子树不为空，则左子树上所有节点的值均小于它的根节点的值； 若它的右子树不空，则右子树上所有节点的值均大于它的根节点的值；它的左右子树也为二叉搜索树。
        '''
        def dfs(root, left, right):
            if root is None:
                return True
            if left < root.val < right:
                return dfs(root.left, left, root.val) and dfs(root.right, root.val, right)
            else:
                return False
        return dfs(root, float('-inf'), float('inf'))
        '''

        # Method 2: 迭代 中序遍历 因为中序遍历得到的二叉搜索树是升序的，所以可以判断遍历完的二叉搜索树是否为升序
        stack = []
        preValue = float('-inf')

        while stack or root is not None:
            while root is not None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= preValue:
                return False
            preValue = root.val
            root = root.right
        return True

# @lc code=end

