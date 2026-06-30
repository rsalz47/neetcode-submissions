# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.recurse_depth(root)

    def recurse_depth(self, node):
        if node == None:
            return 0
        
        left_sum = self.recurse_depth(node.left)
        right_sum = self.recurse_depth(node.right)

        return 1 + max(left_sum, right_sum)