class Solution(object):
    def makesquare(self, matchsticks):
        """
        :type matchsticks: List[int]
        :rtype: bool
        """
        if sum(matchsticks) % 4 != 0:
            return False
        max_length = sum(matchsticks) // 4
        matchsticks.sort(reverse=True)
        sides = [0 for _ in range(4)]
        def dfs(start_index):
            if start_index == len(matchsticks):
                return sides[0] == sides[1] == sides[2] == sides[3] == max_length
            for i in range(4):
                if sides[i] + matchsticks[start_index] <= max_length:
                    sides[i] += matchsticks[start_index]
                    if dfs(start_index + 1):
                        return True
                    sides[i] -= matchsticks[start_index]
            return False
        return dfs(0)
        