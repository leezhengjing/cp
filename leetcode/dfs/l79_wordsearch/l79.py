from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        def get_edges(row, column):
            output = []
            if row + 1 < m:
                output.append((row + 1, column))
            if row - 1 >= 0:
                output.append((row - 1, column))
            if column + 1 < n:
                output.append((row, column + 1))
            if column - 1 >= 0:
                output.append((row, column - 1))
            return output
        def dfs(start_index, row, column):
            if start_index == len(word):
                return True
            valid = False
            for r, c in get_edges(row, column):
                if visited[r][c]: continue
                if board[r][c] == word[start_index]:
                    visited[r][c] = True
                    valid = valid or dfs(start_index + 1, r, c)
                    if valid: return True
                    visited[r][c] = False
                visited
            return valid
        initial_coords = []
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    initial_coords.append((i, j))
        valid = False
        for r, c in initial_coords:
            visited[r][c] = True
            valid = valid or dfs(1, r, c)
            visited[r][c] = False
        return valid

