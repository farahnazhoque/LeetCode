"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Type: Binary Search Tree
"""


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # base case:
        if root is None:
            return 0
        
        # initializing the depth of the two subtrees.
        leftDepth = self.minDepth(root.left)
        rightDepth = self.minDepth(root.right)
        
        # if both the left and right subtrees are empty, we will return 1.
        if root.left is None and root.right is None:
            return 1
        # if the left subtree is empty, we will return the right subtree depth + 1.
        if root.left is None:
            return rightDepth + 1
        # if the right subtree is empty, we will return the left subtree depth + 1.
        if root.right is None:
            return leftDepth + 1    
        
        return min(leftDepth, rightDepth) + 1