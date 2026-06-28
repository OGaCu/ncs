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
        # def dfsHeight(node):
        #     if not node:
        #         return 0
        #     left = dfsHeight(node.left)
        #     right = dfsHeight(node.right)
        #     return 1 + max(left, right)

        # mD1 = dfsHeight(root.left) + dfsHeight(root.right)
        # mD2 = max(self.diameterOfBinaryTree(root.left),
        #         self.diameterOfBinaryTree(root.right))
        # return max(mD1, mD2)


        # DFS O(n) time and O(height) space
        maxDiameter = 0
        def dfs(node):
            nonlocal maxDiameter
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            maxDiameter = max(maxDiameter, left + right)
            return 1 + max (left, right)
        dfs(root)
        return maxDiameter
