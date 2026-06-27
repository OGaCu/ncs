# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        from collections import deque
        queue = deque([root])
        result = []

        if not root: 
            return []

        while queue:
            
            level = []
            levelSize = len(queue)

            
            for _ in range(levelSize):
                current = queue.popleft()
                level.append(current.val)

                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)

            result.append(level)
        return result
        