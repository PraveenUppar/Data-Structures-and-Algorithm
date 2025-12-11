class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        mapping = defaultdict(list)

        for course,precourse in prerequisites:
            mapping[course].append(precourse)
        
        taken = set()

        def dfs(course):

            if not mapping[course]:
                return True

            if course in taken:
                return False

            taken.add(course)

            for precourse in mapping[course]:
                if not dfs(precourse):
                    return False
            
            mapping[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
        