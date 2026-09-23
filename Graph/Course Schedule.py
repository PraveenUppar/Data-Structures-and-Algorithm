# You are given an array prerequisites where prerequisites[i] = [a, b] indicates that you must take course b first if you want to take course a.

# The pair [0, 1], indicates that must take course 1 before taking course 0.

# There are a total of numCourses courses you are required to take, labeled from 0 to numCourses - 1.

# Return true if it is possible to finish all courses, otherwise return false.

from collections import defaultdict

def course(numCourses, prerequisites):

    graph = defaultdict(list)

    for u,v in prerequisites:
        graph[u].append(v)

    visited =set()
    curr_path = set()

    def check(node):

        if node in curr_path:
            return False

        if node in visited:
            return True

        curr_path.add(node)

        for nei_node in graph[node]:
            if not check(nei_node):
                return False

        curr_path.remove(node)
        visited.add(node)
        return True

    for i in range(numCourses):
        if not check(i):
            return False
    return True
