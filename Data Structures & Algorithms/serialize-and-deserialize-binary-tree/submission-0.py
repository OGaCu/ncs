# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # BFS, level order traversal
        q = deque([root])
        res = []
        while q:
            length = len(q)
            for _ in range(length):
                node = q.popleft()
                if not node:
                    res.append("N")
                else:
                    res.append(str(node.val))
                    q.append(node.left)
                    q.append(node.right)
        
        return ",".join(res)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        if vals[0] == "N":
            return None
        root = TreeNode(vals[0])
        q = deque([root])
        idx = 1
        while q and idx < len(vals):
            node = q.popleft()
            if vals[idx] != "N":
                node.left = TreeNode(int(vals[idx]))
                q.append(node.left)
            idx += 1
            # else:
            #     node.left = None
            if idx >= len(vals):
                break
            if vals[idx] != "N":
                node.right = TreeNode(int(vals[idx]))
                q.append(node.right)
            idx += 1
            # else:
            #     node.right = None
            
        return root
