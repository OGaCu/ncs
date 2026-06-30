# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # DFS
        def validate(node, low, high):
            if not node:
                return True
    
            if (low is not None and low >= node.val):
                return False
            
            if (high is not None and high <= node.val):
                return False

            return validate(node.left, low, node.val) and validate(node.right, node.val, high)

        
        return validate(root, None, None)