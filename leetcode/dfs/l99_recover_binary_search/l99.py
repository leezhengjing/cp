from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev = first = second = None
        def dfs(root):
            nonlocal prev, first, second
            if root is None:
                return
            dfs(root.left)
            if prev and prev.val > root.val:
                if first is None:
                    first = prev
                second = root
            prev = root
            dfs(root.right)
        dfs(root)
        first.val, second.val = second.val, first.val

# Initial attempt, wrong, passed like 357/1919 cases
# def recoverTree(self, root: Optional[TreeNode]) -> None:
#     """
#     Do not return anything, modify root in-place instead.
#     """
#     def dfs(root, min_val, max_val):
#         if root is None:
#             return None
#         if root.val < min_val or root.val > max_val:
#             return root
#         left = dfs(root.left, min_val, root.val)
#         if left:
#             return left
#         else:
#             return dfs(root.right, root.val, max_val)
#     misplaced_node = dfs(root, float('-inf'), float('inf'))
#     temp = root.val
#     root.val = misplaced_node.val
#     misplaced_node.val = temp