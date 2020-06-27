#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] 二叉树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Method 1: Recursion
        '''
        if root == None:
            return None
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p ,q)
        if not left: 
            return right
        if not right:
            return left
        return root
        '''

        # Method 2: Save Parent Node
        parent = {}
        visited = set()

        def dfs(root):
            if root.left != None:
                parent[root.left] = root # root.left指的是root的左子节点，root.left.val指的是左子节点的值
                dfs(root.left)
            if root.right != None:
                parent[root.right] = root
                dfs(root.right)

        dfs(root)
        while p != None:
            visited.add(p) # 要把自己加进去 否则如果p是q的父节点的话 检查不到p存在
            p = parent.get(p)

        while q != None:
            if q in visited:
                return q
            q = parent.get(q)
        return None

# @lc code=end

