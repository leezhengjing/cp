class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = [[],[],["a","b","c"],["d","e","f"],["g","h","i"],["j","k","l"],["m","n","o"],["p","q","r","s"],["t","u","v"],["w","x","y","z"]]
        def dfs(start_index, path):
            if start_index == len(digits):
                res.append(''.join(path))
                return
            for letter in letters[int(digits[start_index])]:
                path.append(letter)
                dfs(start_index + 1, path)
                path.pop()
        res = []
        if digits == "":
            return res
        dfs(0, [])
        return res