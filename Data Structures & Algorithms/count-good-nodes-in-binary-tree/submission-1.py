class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxVal):
            if not node:
                return 0

            good = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)

            return (
                good
                + dfs(node.left, maxVal)
                + dfs(node.right, maxVal)
            )

        return dfs(root, root.val)