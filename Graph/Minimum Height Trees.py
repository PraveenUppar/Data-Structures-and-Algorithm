# A tree is an undirected graph in which any two vertices are connected by exactly one path. 
# In other words, any connected graph without simple cycles is a tree.

# You are given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges 
# where edges[i] = [a[i], b[i]] indicates that there is an undirected edge between the two nodes a[i] and b[i] in the tree, 
# you can choose any node of the tree as the root. 
# When you select a node x as the root, the result tree has height h. 
# Among all possible rooted trees, those with minimum height (i.e. min(h)) are called minimum height trees (MHTs).

# Return a list of all MHTs' root labels. You can return the answer in any order.

# The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

from collections import defaultdict

def findheights(n, edges):

    graph = defaultdict(list)

    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)

    def checkheight(node, visited):
        height = 0
        visited.add(node)

        for nei_node in graph[node]:
            if nei_node not in visited:
                height = max(height, 1 + checkheight(nei_node, visited))

        return height

    heights = []

    for i in range(n):
        visited = set()
        heights.append(checkheight(i, visited))

    min_height_tree = min(heights)
    min_heights = []

    for i in range(len(heights)):
        if heights[i] == min_height_tree:
            min_heights.append(i)

    return min_heights

    