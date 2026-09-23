# You are given a 0-indexed integer array nums, and you are allowed to traverse between its indices. 
# You can traverse between index i and index j, i != j, if and only if gcd(nums[i], nums[j]) > 1, where gcd is the greatest common divisor.

# Your task is to determine if for every pair of indices i and j in nums, where i < j, there exists a sequence of traversals that can take us from i to j.

# Return true if it is possible to traverse between all such pairs of indices, or false otherwise.

import math
from collections import defaultdict

def traversal(nums):

    graph = defaultdict(list)

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if math.gcd(nums[i], nums[j]) > 1:
                graph[i].append(j)
                graph[j].append(i)

    visited = set()

    def explore(node):

        visited.add(node)

        for nei_node in graph[node]:
            if nei_node not in visited:
                explore(nei_node)

    explore(0)
    return len(visited) == len(nums)