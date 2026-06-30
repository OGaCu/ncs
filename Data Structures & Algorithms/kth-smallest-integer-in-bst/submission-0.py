# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # traverse the entire tree to put node values into list
        # then sort, O(n log n)

        # nature of BST, we search left subtree first for smallest number
        # DFS
        # we keep a in-order traversal
        # traverse until k nodes are visited
        result = []
        def inorder(node):
            if not node:
                return

            inorder(node.left)
            result.append(node.val)
            inorder(node.right)

        inorder(root)
        return result[k - 1]
