class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        n = len(s)
        def dfs(start_index, path):
            if start_index == n:
                res.append(" ".join(path))
                return
            for end_index in range(start_index, n):
                word = s[start_index:end_index + 1]
                # + 1 because slice is non inclusive of end
                if word in wordDict:
                    path.append(word)
                    dfs(start_index + len(word), path)
                    path.pop()
        res = []
        dfs(0, [])
        return res 