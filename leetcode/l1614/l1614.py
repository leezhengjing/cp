class Solution:
    def maxDepth(self, s: str) -> int:
        counter = 0
        max_so_far = 0
        for char in s:
            if char == "(":
                counter += 1
                max_so_far = max(max_so_far, counter)
            if char == ")":
                counter -= 1
        return max_so_far