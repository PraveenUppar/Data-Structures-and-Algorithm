class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        mapping = defaultdict(list)

        for course,precourse in prerequisites:
            mapping[course].append(precourse)
        
        state = [0] * numCourses
        # 0 = Unvisited
        # 1 = Visiting
        # 2 = Done
        res = []

        def dfs(course):

            if state[course] == 1:
                return False
            
            if state[course] == 2:
                return True
            
            state[course] = 1

            for precourse in mapping[course]:
                if not dfs(precourse):
                    return False

            state[course] = 2
            res.append(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return res
        