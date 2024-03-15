# First Try, without help
from typing import List

def permutations(letters: str) -> List[str]:
    # WRITE YOUR BRILLIANT CODE HERE
    n = len(letters)
    def dfs(start_index, path, remaining):
        if start_index == n:
            res.append(path)
            return
        for letter in remaining:
            dfs(start_index + 1, path + letter, remaining.replace(letter, ''))
    res = []
    dfs(0, '', letters)
    return res
        

if __name__ == '__main__':
    letters = input()
    res = permutations(letters)
    for line in sorted(res):
        print(line)
