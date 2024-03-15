def permutations(letters):
    def dfs(start_index, path, used):
        if start_index == len(letters):
            res.append(''.join(path))
            return
        for i, letter in enumerate(letters):
            if used[i]:
                continue
            path.append(letter)
            used[i] = True
            dfs(start_index + 1, path, used)
            # dfs(start_index + 1, path + [num], used) , In the case of numbers where we cant .join(), have to just add []
            path.pop()
            used[i] = False
            
    res = []
    dfs(0, [], [False] * len(letters))
    return res

if __name__ == '__main__':
    letters = input()
    res = permutations(letters)
    for line in sorted(res):
        print(line)
