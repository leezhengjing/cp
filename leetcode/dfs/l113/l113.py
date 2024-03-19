# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        def dfs(root, path, remaining):
            if root is None:
                return
            path.append(root.val)
            remaining -= root.val
            if root.left is None and root.right is None and remaining == 0:
                res.append(path[:])
            else:
                dfs(root.left, path, remaining)
                dfs(root.right, path, remaining)
            path.pop()
        res = []
        dfs(root, [], targetSum)
        return res