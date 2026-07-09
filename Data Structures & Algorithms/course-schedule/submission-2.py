class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # topological sort
        indegree = {i:0 for i in range(numCourses)}
        adj = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            indegree[pre] += 1 # edge coming in to crs
            adj[crs].append(pre)
        
        queue = deque([crs for crs in indegree if indegree[crs] == 0])
        finished = set()
        while queue:
            crs = queue.popleft()
            finished.add(crs)
            for pre in adj[crs]:
                indegree[pre] -= 1
                if indegree[pre] == 0:
                    queue.append(pre)
        
        return len(finished) == numCourses