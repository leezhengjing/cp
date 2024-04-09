from collections import deque
from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        queue = deque([root])
        res = []
        while len(queue) > 0:
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                if i == n - 1:
                    res.append(node.val)
                for child in [node.left, node.right]:
                    if child:
                        queue.append(child)
        return res