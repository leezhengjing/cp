# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        def dfs(root, remaining):
            if root is None:
                return False
            remaining -= root.val
            contains_ans = False
            if root.left is None and root.right is None and remaining == 0:
                return True
            else:
                contains_ans = dfs(root.left, remaining) or dfs(root.right, remaining)
            return contains_ans
        return dfs(root, targetSum)
                