from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()
        def dfs(start_index, path, rem):
            if rem == 0:
                res.append(path[:])
                return
            for i in range(start_index, n):
                if candidates[i] > rem:
                    break
                if i > start_index and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                dfs(i + 1, path, rem - candidates[i])
                path.pop()
        res = []
        dfs(0, [], target)
        return res