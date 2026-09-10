# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def averageOfSubtree(self, root: TreeNode) -> int:
        self.mm = 0

        def postorder(node):
            if not node:
                return 0, 0

            ls, lc = postorder(node.left)
            rs, rc = postorder(node.right)

            tot = ls + rs + node.val
            tc = lc + rc + 1

            if tot // tc == node.val:
                self.mm += 1

            return tot, tc

        postorder(root)
        return self.mm