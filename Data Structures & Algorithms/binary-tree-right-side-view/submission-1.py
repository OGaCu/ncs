# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        from collections import deque

        queue = deque([root])

        while queue:
            levelStack = []
            levelSize = len(queue)

            for _ in range(levelSize):  # for each child
                node = queue.popleft()

                levelStack.append(node)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            rightNode = levelStack.pop()

            result.append(rightNode.val)

        return result
