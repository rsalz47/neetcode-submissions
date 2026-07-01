class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def recurse_count(node):
            nonlocal diameter
            if not node:
                return 0

            left = recurse_count(node.left)
            right = recurse_count(node.right)

            # update the best diameter seen so far
            diameter = max(diameter, left + right)

            # return height of this subtree
            return 1 + max(left, right)

        recurse_count(root)
        return diameter
