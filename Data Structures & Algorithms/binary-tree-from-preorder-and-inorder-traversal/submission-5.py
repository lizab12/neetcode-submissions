class Solution:
    def buildTree(
        self,
        preorder: List[int],
        inorder: List[int]
    ) -> Optional[TreeNode]:

        h = {}
        for i in range(len(inorder)):
            h[inorder[i]] = i

        pre = 0

        def search(left, right):
            nonlocal pre

            if left > right:
                return None

            root_val = preorder[pre]
            pre += 1

            root = TreeNode(root_val)

            mid = h[root_val]

            root.left = search(left, mid - 1)
            root.right = search(mid + 1, right)

            return root

        return search(0, len(inorder) - 1)