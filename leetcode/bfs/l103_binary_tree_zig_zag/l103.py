# Definition for a binary tree node.
from collections import deque
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        
        queue = deque([root])
        left_to_right = True
        while len(queue) > 0:
            n = len(queue)
            temp = deque()
            for _ in range(n):
                node = queue.popleft()
                if node is None:
                    return res
                for child in [node.left, node.right]:
                    if child is not None:
                        queue.append(child)
                if left_to_right:
                    temp.append(node.val)
                else:
                    temp.appendleft(node.val)
            res.append(temp)
            left_to_right = not left_to_right
        return res