class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        n = len(s)
        def dfs(start_index):
            if start_index == n:
                return True
            if start_index in memo:
                return memo[start_index]
            ans = False
            for end_index in range(start_index, n):
                if s[start_index: end_index + 1] in wordDict:
                    if dfs(end_index + 1):
                        ans = True
                        break
            memo[start_index] = ans
            return ans
        return dfs(0)