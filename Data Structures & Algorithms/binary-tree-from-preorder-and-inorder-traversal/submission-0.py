# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # build recursively
        # first value of preorder is always the root
        # find root in inorder to partition left subtree and rightsubtree

        if not preorder or not inorder:
            return
        root = TreeNode(preorder[0])

        rootIdx = inorder.index(root.val)

        right = len(inorder) - rootIdx
        left = rootIdx

        root.left = self.buildTree(preorder[1:1+ left], inorder[:rootIdx] )
        root.right = self.buildTree(preorder[1 + left:1+left+right], inorder[left + 1:left + 1 + right])

        return root