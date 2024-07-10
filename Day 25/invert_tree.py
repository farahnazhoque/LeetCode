# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # understanding
        # we are given a tree, where we have to swap all the right nodes with the left nodes, and vice versa


        # matching
        # pointers 


        # planning
        """
        if not root:
            return None
        
        """


        # implementing
        if not root:
            return None

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


        # reviewing: correct


        # evaluating
        # Time complexity: O(n)
        # Space complexity: O(n)