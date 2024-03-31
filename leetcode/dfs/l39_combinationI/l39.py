from typing import List

def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    # WRITE YOUR BRILLIANT CODE HERE
    candidates.sort()
    def dfs(start_index, path, remaining):
        if remaining == 0:
            res.append(path[:])
            return
        for i in range(start_index, len(candidates)):
            if remaining - candidates[i] < 0: break
            if i > 0 and candidates[i] == candidates[i-1]: continue
            path.append(candidates[i])
            dfs(i, path, remaining - candidates[i])
            path.pop()
    res = []
    dfs(0, [], target)
    return res

if __name__ == '__main__':
    candidates = [int(x) for x in input().split()]
    target = int(input())
    res = combination_sum(candidates, target)
    for lst in res:
        lst.sort()
    for lst in sorted(res):
        print(' '.join(map(str, lst)))
