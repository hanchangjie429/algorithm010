#
# @lc app=leetcode.cn id=429 lang=python3
#
# [429] N叉树的层序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
import collections
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        # Method 1:队列 广度优先算法
        # 用一个列表存放节点值，队列存放节点。首先将根节点放到队列中，当队列不为空时，则在队列取出一个节点，并将其子节点添加到队列中。
        if root is None:
           return []
        res = []
        queue = collections.deque([root])
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                queue.extend(node.children)
            res.append(level)
        return res
# @lc code=end

