class Trie:
    def __init__(self):
        self.children = {}
        self.end = False
        self.word = None

    def addWord(self, word):
        cur = self

        for c in word:
            if c not in cur.children:
                cur.children[c] = Trie()
            cur = cur.children[c]

        cur.end = True
        cur.word = word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        root = Trie()

        # Build Trie from words
        for word in words:
            root.addWord(word)

        rows = len(board)
        cols = len(board[0])

        res = []
        visit = set()

        def dfs(i, j, node):

            # out of bounds or already visited
            if (
                i < 0 or i >= rows or
                j < 0 or j >= cols or
                (i, j) in visit
            ):
                return

            char = board[i][j]

            # character not in current Trie path
            if char not in node.children:
                return

            node = node.children[char]

            if node.end:
                res.append(node.word)
                node.end = False   # avoid duplicates

            visit.add((i, j))

            dfs(i + 1, j, node)
            dfs(i - 1, j, node)
            dfs(i, j + 1, node)
            dfs(i, j - 1, node)

            visit.remove((i, j))

        for i in range(rows):
            for j in range(cols):
                dfs(i, j, root)

        return res