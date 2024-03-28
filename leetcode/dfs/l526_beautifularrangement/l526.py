class Solution(object):
    def countArrangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        def dfs(start_index, visited):
            if start_index == n + 1:
                return 1
            ways = 0
            for i in range(1, n + 1):
                if (not visited[i]) and (start_index % i == 0 or i % start_index == 0):
                    visited[i] = True
                    ways += dfs(start_index + 1, visited)
                    visited[i] = False
            return ways
        visited = [False for _ in range(n+1)]
        return dfs(1, visited)