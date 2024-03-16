class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        memo = {}
        def dfs(start_index, memo):
            if start_index in memo:
                return memo[start_index]
            if start_index == len(s):
                return 1
            ways = 0
            if s[start_index] == '0':
                return ways
            ways += dfs(start_index + 1, memo)
            if 10 <= int(s[start_index: start_index + 2]) <= 26:
                ways += dfs(start_index + 2, memo)
            memo[start_index] = ways
            return ways
        return dfs(0, memo)