# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        inOrder = []
        def inOrderT(node):
            if not node:
                return
            inOrderT(node.left)
            inOrder.append(node.val)
            inOrderT(node.right)
        inOrderT(root)
        for i in range(1,len(inOrder)):
            if inOrder[i-1]>=inOrder[i]:
                return False
        return True
        