class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None

        if p.val == root.val or q.val == root.val:
            return root

        searchLeft = self.search(root.left, p, q)
        searchRight = self.search(root.right, p, q)

        if searchLeft == 2:
            return self.lowestCommonAncestor(root.left, p, q)

        if searchRight == 2:
            return self.lowestCommonAncestor(root.right, p, q)

        if searchLeft > 0 and searchRight > 0:
            return root

        return None

    def search(self, root: TreeNode, p: TreeNode, q: TreeNode) -> int:
        if not root:
            return 0

        count = 0

        if root.val == p.val:
            count += 1

        if root.val == q.val:
            count += 1

        count += self.search(root.left, p, q)
        count += self.search(root.right, p, q)

        return count