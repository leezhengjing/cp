class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        visited = [False for _ in range(n)]
        nums.sort()
        def dfs(start_index, path):
            if start_index == n:
                res.append(path[:])
                return
            for i in range(n):
                if visited[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                    continue
                path.append(nums[i])
                visited[i] = True
                dfs(start_index + 1, path)
                path.pop()
                visited[i] = False
        res = []
        dfs(0, [])
        return res