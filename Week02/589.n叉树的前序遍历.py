#
# @lc app=leetcode.cn id=589 lang=python3
#
# [589] N叉树的前序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        # Method 1: 递归方法
        '''
        res = []
        if not root:
            return []        
        def helper(root):
            res.append(root.val)
            for child in root.children:
                helper(child)
        helper(root)
        return res
        '''

        # Method 2: 迭代方法
        
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.children:
                # 这里用到了倒序循环
                for child in reversed(node.children): 
                    stack.append(child)
        return res
        
# @lc code=end

