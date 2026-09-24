class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        r = []
        q = collections.deque()
        q.append(root)

        while q:
            qL = len(q)
            l = []

            for i in range(qL):
                node = q.popleft()
                l.append(node.val)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            r.append(l)

        return r