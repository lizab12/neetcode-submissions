# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        rightH = self.maxHeight(root.right)
        leftH = self.maxHeight(root.left)
        if abs(leftH - rightH) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def maxHeight(self, root: Optional[TreeNode])->int:
        if not root:
            return 0
        return 1+max(self.maxHeight(root.left), self.maxHeight(root.right))
        