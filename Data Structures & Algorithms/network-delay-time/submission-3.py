class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        import heapq
        # dijkstra's
        # find shortest path to all nodes from the source node k
        # given total node: 1, 2, ..., n

        # create adjacency list for times
        adj = collections.defaultdict(list)
        for s, t, weight in times:
            adj[s].append((t, weight))
        
        minHeap = [(0, k)] # time, node
        visited = set()
        t = 0
        while minHeap:
            time, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            t = time
            visited.add(node)
            
            # add all neighbor of node to heap
            for target, weight in adj[node]:
                if target not in visited:
                    heapq.heappush(minHeap, (weight + time, target))

            # if len(visited) == n:
            #     # return the max time used
            #     return t
        
        return t if len(visited) == n else -1 # some nodes unreachable

        # distance from source to all nodes
        # dist = float('inf') * n 

        # dist[k] = 0
