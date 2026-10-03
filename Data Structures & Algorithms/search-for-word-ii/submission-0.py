class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


class Solution:
    def findWords(self, board, words):

        root = TrieNode()

        # build trie
        for word in words:
            cur = root

            for c in word:
                if c not in cur.children:
                    cur.children[c] = TrieNode()

                cur = cur.children[c]

            cur.end = True

        ROWS = len(board)
        COLS = len(board[0])

        result = []
        visited = set()

        def dfs(r, c, node, path):

            if (
                r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                (r, c) in visited or
                board[r][c] not in node.children
            ):
                return

            ch = board[r][c]

            node = node.children[ch]
            path += ch

            if node.end:
                result.append(path)

                # 防止同一个 word 被重复加入
                node.end = False

            visited.add((r, c))

            dfs(r + 1, c, node, path)
            dfs(r - 1, c, node, path)
            dfs(r, c + 1, node, path)
            dfs(r, c - 1, node, path)

            visited.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return result