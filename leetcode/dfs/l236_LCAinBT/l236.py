# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root):
            if root is None:
                return None
            if root == p or root == q:
                return root
            left = dfs(root.left)
            right = dfs(root.right)
            if not left is None and not right is None:
                return root
            elif not left is None and right is None:
                return left
            elif left is None and not right is None:
                return right
        return dfs(root)
        