class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        root = TrieNode()

        # 把字典中的单词加入 Trie
        for word in dictionary:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_word = True

        n = len(s)

        # dp[i]：从 s[i] 开始到末尾，最少有多少个多余字符
        # dp[n] = 0：空字符串没有多余字符
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            # 选择一：把当前字符当作多余字符
            dp[i] = 1 + dp[i + 1]

            # 选择二：从当前位置开始，沿 Trie 匹配单词
            node = root
            for j in range(i, n):
                if s[j] not in node.children:
                    break

                node = node.children[s[j]]

                # s[i:j+1] 是完整单词，这一段不产生多余字符
                if node.is_word:
                    dp[i] = min(dp[i], dp[j + 1])

                # 不立即停止，继续找可能存在的更长单词

        return dp[0]