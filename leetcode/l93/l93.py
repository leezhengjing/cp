class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
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

        