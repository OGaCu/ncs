# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # BST: left subtree < node < right subtree
        # assume p is the smaller value
        p.val, q.val = min(p.val, q.val), max(p.val, q.val)

        # p needs its anscester, where p is its left node
        # q is its rightsubtree

       # 2 scenarios
       # p and q in diff subtree: LCA in split
       # tutorial video
        if p.val < root.val and root.val < q.val: # split is found
            return root

        if p.val == root.val or q.val == root.val:
            return root

        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)


        
        

