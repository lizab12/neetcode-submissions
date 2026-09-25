# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        h = {}
        for i in range(len(inorder)):
            h[inorder[i]]=i
        pre = 0
        def search(left, right):
            nonlocal pre
            if left > right:
                return None
            root_val = preorder[pre]
            root = TreeNode(preorder[pre])
            pre+=1
            mid = h[root_val]
            root.left = search(left, mid-1)
            root.right = search(mid+1, right)
            return root
        return search(0,len(inorder)-1)

