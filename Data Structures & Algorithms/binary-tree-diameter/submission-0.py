# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        rightH = self.maxHeight(root.right)
        leftH = self.maxHeight(root.left)
        d = leftH+rightH
        sub = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
        return max(d,sub)

    def maxHeight(self, root: Optional[Treenode]):
        if not root:
            return 0
        return 1+max(self.maxHeight(root.left), self.maxHeight(root.right))
        