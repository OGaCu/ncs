# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # find same value of root
        def bfs(r1, r2):
            if not r1 and not r2:
                return True
            if not r1 or not r2:
                return False
            if r1.val == r2.val:
                l = bfs(r1.left, r2.left)
                r = bfs(r1.right, r2.right)
                return l and r
            return False

        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False

        # if root.val == subRoot.val:
        #     return bfs(root, subRoot)
        if bfs(root, subRoot):
            return True
        else:
            left = self.isSubtree(root.left, subRoot)
            right = self.isSubtree(root.right, subRoot)
            return left if left else right
