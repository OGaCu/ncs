class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # time and space O(V + E) where V is numCourses, E is len(prereq)
        # DFS
        prereqMap = {i:[] for i in range(numCourses)}

        for course, prereq in prerequisites:
            prereqMap[course].append(prereq)

        visitSet = set() # return false bcuz loop
        def dfs(crs):
            if crs in visitSet:
                return False
            if prereqMap[crs] == []:
                return True
            
            visitSet.add(crs)
            for pre in prereqMap[crs]:
                if not dfs(pre): return False

            visitSet.remove(crs)
            prereqMap[crs] = []
            return True
        
        for crs in range(numCourses): # need to call on every node to cover disconnected component
            if not dfs(crs):
                return False

        return True