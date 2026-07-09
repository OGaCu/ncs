class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # topological sort
        # time and space O(V + E)
        # prereq = [0, 1] means need to take 1 in order to take 0, 0 <- 1
        indegree = {i:0 for i in range(numCourses)}
        adj = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            indegree[pre] += 1 # edge coming in to pre
            adj[crs].append(pre) # notice the edge direction from prereq
        
        queue = deque([crs for crs in indegree if indegree[crs] == 0])
        finished = 0
        while queue:
            crs = queue.popleft()
            finished += 1
            for pre in adj[crs]:
                indegree[pre] -= 1
                if indegree[pre] == 0:
                    queue.append(pre)
        
        return finished == numCourses