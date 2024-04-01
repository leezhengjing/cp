from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node is None:
                return 0, True
            left_height, left_balanced = dfs(node.left)
            right_height, right_balanced = dfs(node.right)
            subtree_height = max(left_height, right_height) + 1
            is_balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
            return subtree_height, is_balanced
        return dfs(root)[1]