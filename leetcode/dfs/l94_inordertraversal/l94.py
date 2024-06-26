from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(root):
            if root is None:
                return
            left = dfs(root.left)
            res.append(root.val)
            right = dfs(root.right)
        dfs(root)
        return res
            