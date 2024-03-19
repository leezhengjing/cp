"""Question 1 of 10
A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.

Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s. You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.

Example 1:

Input: s = "25525511135"

Output: ["255.255.11.135","255.255.111.35"]

Example 2:

Input: s = "0000"

Output: ["0.0.0.0"]

Example 3:

Input: s = "101023"

Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]

Constraints:

1 <= s.length <= 20
s consists of digits only."""
from typing import List
def restoreIpAddresses(s : str) -> List[str]:
    def get_edges(start_index):
        edges = []
        for i in range(start_index, start_index + 3):
            edges.append(s[start_index:i + 1])
        return edges
    def is_valid(edge):
        if edge == "0": return True
        elif edge[0] == "0": return False
        elif int(edge) > 255: return False
        else: return True
    def dfs(start_index, path):
        if len(path) > 4:
            return
        if start_index == len(s):
            if len(path) == 4:
                res.add('.'.join(path))
            return
        for edge in get_edges(start_index):
            if not is_valid(edge):
                continue
            path.append(edge)
            dfs(start_index + len(edge), path)
            path.pop()
    res = set()
    dfs(0, [])
    return list(res)

if __name__ == "__main__":
    "Test case 1"
    s = "25525511135"
    print("Expected: [255.255.11.135, 255.255.111.35]")
    print("Output:", restoreIpAddresses(s))