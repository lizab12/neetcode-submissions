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
        def insert(root):
            if not root:
                return
            h.append(root.val)
            insert(root.left)
            insert(root.right)
        m = -1
        insert(root)
        heapq.heapify(h)
        for i in range(k):
            m = heapq.heappop(h)
        return m

        