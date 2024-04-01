# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        def dfs(root):
            if root is None:
                return TreeNode(val)
            if val < root.val:
                root.left = dfs(root.left)
            else:
                root.right = dfs(root.right)
            return root

        return dfs(root)