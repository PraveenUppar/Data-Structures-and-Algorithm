# You are given an array prerequisites where prerequisites[i] = [a, b] indicates that you must take course b first if you want to take course a.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# There are a total of numCourses courses you are required to take, labeled from 0 to numCourses - 1.

# Return a valid ordering of courses you can take to finish all courses. If there are many valid answers, return any of them. 
# If it's not possible to finish all courses, return an empty array.


from collections import defaultdict

def course(numCourses, prerequisites):

    graph = defaultdict(list)

    for u,v in prerequisites:
        graph[u].append(v)

    visited =set()
    curr_path = set()

    res = []

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
        res.append(node)
        return True

    for i in range(numCourses):
        if not check(i):
            return []
    return res
