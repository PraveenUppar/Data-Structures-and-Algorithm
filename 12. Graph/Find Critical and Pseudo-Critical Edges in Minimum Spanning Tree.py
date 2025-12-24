class UnionFind:
    def __init__(self, n):
        self.n = n
        self.Parent = list(range(n + 1))
        self.Size = [1] * (n + 1)

    def find(self, node):
        if self.Parent[node] != node:
            self.Parent[node] = self.find(self.Parent[node])
        return self.Parent[node]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False
        self.n -= 1
        if self.Size[pu] < self.Size[pv]:
            pu, pv = pv, pu
        self.Size[pu] += self.Size[pv]
        self.Parent[pv] = pu
        return True

    def isConnected(self):
        return self.n == 1

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        for i, e in enumerate(edges):
            e.append(i)
        edges.sort(key = lambda e : e[2])

        def findMST(index, include):
            uf = UnionFind(n)
            wgt = 0
            if include:
                wgt += edges[index][2]
                uf.union(edges[index][0], edges[index][1])

            for i, e in enumerate(edges):
                if i == index:
                    continue
                if uf.union(e[0], e[1]):
                    wgt += e[2]
            return wgt if uf.isConnected() else float("inf")

        mst_wgt = findMST(-1, False)
        critical, pseudo = [], []
        for i, e in enumerate(edges):
            if mst_wgt < findMST(i, False):
                critical.append(e[3])
            elif mst_wgt == findMST(i, True):
                pseudo.append(e[3])

        return [critical, pseudo]
    

# class Solution:
#     def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:

#         for i, edge in enumerate(edges):
#             edge.append(i)

#         adj = defaultdict(list)
#         for u, v, w, idx in edges:
#             adj[u].append((v, w, idx))
#             adj[v].append((u, w, idx))

#         def minimax(src, dst, exclude_idx):
#             dist = [float('inf')] * n
#             dist[src] = 0
#             pq = [(0, src)]

#             while pq:
#                 max_w, u = heappop(pq)
#                 if u == dst:
#                     return max_w

#                 for v, weight, edge_idx in adj[u]:
#                     if edge_idx == exclude_idx:
#                         continue
#                     new_w = max(max_w, weight)
#                     if new_w < dist[v]:
#                         dist[v] = new_w
#                         heappush(pq, (new_w, v))

#             return float('inf')

#         critical, pseudo = [], []

#         for i, (u, v, w, idx) in enumerate(edges):
#             if w < minimax(u, v, idx):
#                 critical.append(idx)
#             elif w == minimax(u, v, idx):
#                 pseudo.append(idx)

#         return [critical, pseudo]
