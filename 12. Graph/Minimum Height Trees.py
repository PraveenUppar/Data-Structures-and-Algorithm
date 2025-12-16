class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        adj = [[] for _ in range(n)]

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node,parent):
            height = 0

            for nei in adj[node]:
                if nei == parent:
                    continue
                height = max(height, 1 + dfs(nei,node))
            return height

        min_height = n
        res = []

        for i in range(n):
            curr_height = dfs(i,-1)
            if curr_height == min_height:
                res.append(i)
            elif curr_height < min_height:
                res = [i]
                min_height = curr_height
        return res
