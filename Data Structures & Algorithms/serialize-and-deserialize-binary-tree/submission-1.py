class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        s = []

        def dfs(root):
            if not root:
                s.append("N")
                return

            s.append(str(root.val))
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return ",".join(s)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None

        vals = data.split(",")
        self.i = 0

        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None

            node = TreeNode(int(vals[self.i]))
            self.i += 1

            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()