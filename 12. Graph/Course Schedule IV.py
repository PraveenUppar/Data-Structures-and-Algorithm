class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        adj = [[] for _ in range(numCourses)]  # [ [adj0], [adj1], [adj2] ]
        for u, v in prerequisites:    # [[1,2],[1,0],[2,0]]
            adj[u].append(v)          # [ adj0 [] adj1 [2,0] adj2 [0] ]
        
        res = []

        def dfs(node, target):
            if node == target:
                return True
            for nei in adj[node]:
                if dfs(nei, target):
                    return True
            return False
        
        for u,v in queries:
            res.append(dfs(u,v))   # [[1,0],[1,2]]
        return res