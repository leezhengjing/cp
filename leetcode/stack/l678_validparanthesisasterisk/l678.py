class Solution:
    def checkValidString(self, s: str) -> bool:
        open_paran = 0
        for char in s:
            if char in '(*':
                open_paran += 1
                continue
            if char == ')' and open_paran > 0:
                open_paran -= 1
                continue
            else:
                return False
        closed_paran = 0
        for char in s[::-1]:
            if char in ')*':
                closed_paran += 1
                continue
            if char == '(' and closed_paran > 0:
                closed_paran -= 1
                continue
            else:
                return False
        return True
            