# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        h = []
        curr = root
        while h or curr:
            while curr:
                h.append(curr)
                curr = curr.left
            m = h.pop()
            k-=1
            if k==0:
                return m.val
            curr = m.right


        