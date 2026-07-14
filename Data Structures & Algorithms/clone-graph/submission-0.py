"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # bfs
        if not node:
            return None

        queue = deque([node])
        deepcopy = {} # node.val : Node()
        deepcopy[node.val] = Node(node.val)

        while queue:
            n = queue.popleft()
            # if n.val in deepcopy:
            #     continue
            # deepcopy[n.val] = Node(n.val, n.neighbors)
            for nei in n.neighbors:
                if nei.val not in deepcopy:
                    queue.append(nei)
                    deepcopy[nei.val] = Node(nei.val)
                deepcopy[n.val].neighbors.append(deepcopy[nei.val])

        return deepcopy[node.val]