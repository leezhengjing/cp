from collections import deque
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        queue = deque([root])
        res = 0
        while len(queue) > 0:
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                if node.left is None and node.right is None:
                    res += 1
                    return res
                for child in [node.left, node.right]:
                    if child:
                        queue.append(child)
            res += 1
        return res