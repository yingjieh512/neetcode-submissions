class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        # 字符串长度
        n = len(s)

        # dp[i] 表示前 i 个字符能不能被成功拆分
        # 一共需要 n + 1 个位置，包括空字符串
        dp = [False] * (n + 1)

        # 空字符串不需要任何单词，所以视为成功
        dp[0] = True

        # 遍历每个前缀长度 i
        for i in range(1, n + 1):

            # 尝试让字典中的每个单词作为最后一个单词
            for word in wordDict:

                # 当前单词长度
                length = len(word)

                # 条件 1：当前前缀必须能容纳这个单词
                if i >= length:

                    # 条件 2：前面的字符串已经能被拆分
                    # 条件 3：最后 length 个字符等于当前单词
                    if dp[i - length] and s[i - length:i] == word:

                        # 前半部分能拆，后半部分是合法单词
                        # 所以前 i 个字符也能成功拆分
                        dp[i] = True

                        # 已经找到一种合法拆分，不需要继续尝试
                        break

        # 判断整个字符串能不能拆分
        return dp[n]