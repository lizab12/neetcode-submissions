class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        c = 0

        q = collections.deque()
        q.append((root, root.val))

        while q:
            node, maxVal = q.popleft()

            if node.val >= maxVal:
                c += 1

            newMax = max(maxVal, node.val)

            if node.left:
                q.append((node.left, newMax))

            if node.right:
                q.append((node.right, newMax))

        return c