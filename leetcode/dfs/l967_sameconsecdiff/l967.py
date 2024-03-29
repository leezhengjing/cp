class Solution(object):
    def numsSameConsecDiff(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        def dfs(start_index, path):
            if start_index == n:
                res.append(path)
                return
            last_added = path % 10
            if last_added - k >= 0:
                dfs(start_index + 1, path * 10 + (last_added - k))
            if last_added + k <= 9 and k != 0:
                dfs(start_index + 1, path * 10 + (last_added + k))
        res = []
        for i in range(1, 10):
            dfs(1, i)
        return res