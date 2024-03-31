class Solution:
    def grayCode(self, n: int) -> List[int]:
        length = 1 << n
        visited = [False] * length
        def dfs(start_index, prev_code):
            if start_index == length:
                return True
            for i in range(n):
                next_code = prev_code ^ (1 << i)
                if not visited[next_code]:
                    path.append(next_code)
                    visited[next_code] = True
                    if dfs(start_index + 1, next_code): return True
                    visited[next_code] = False
                    path.pop()  
            return False
        path = [0]
        visited[0] = True
        dfs(1, 0)
        return path