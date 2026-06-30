# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        # root is always considered good
        
        # brute force
        # keep track of path nodes
        # then compare current node value with paths nodes
        
        # we need to track the largest value on the path 
        numGoods = 0

        def dfs(node, maxPath):
            nonlocal numGoods
            if not node:
                return
            
            if node.val >= maxPath:
                print(node.val, maxPath)
                numGoods += 1
            
            maxPath = max(maxPath, node.val)
            
            dfs(node.left, maxPath)
            dfs(node.right, maxPath)

        dfs(root, float('-inf'))
        return numGoods
        
        
        