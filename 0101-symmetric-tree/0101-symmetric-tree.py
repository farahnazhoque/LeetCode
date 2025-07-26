# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isMirror(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return left.val == right.val and self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # Understanding
        '''
        we have to check if the values of left and right match, and if they are the root node, skip
        '''

        # Matching
        '''
        linked list
        '''

        # Planning

        # Implementing
        if not root:
            return True
        return self.isMirror(root.left, root.right)
        

        # Reviewing