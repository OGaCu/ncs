# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # O(n^2) brute force
        def dfsHeight(node):
            if not node:
                return 0
            left = dfsHeight(node.left)
            right = dfsHeight(node.right)
            return 1 + max(left, right)

        maxDiameter = dfsHeight(root.left) + dfsHeight(root.right)
        mD2 = max(self.diameterOfBinaryTree(root.left),
                self.diameterOfBinaryTree(root.right))
        return max(maxDiameter, mD2)
