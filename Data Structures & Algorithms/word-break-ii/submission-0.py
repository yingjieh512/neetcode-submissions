class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)
        res=[]
        path=[]
        def dfs(start):
            if start==len(s):
                res.append(" ".join(path))
                return
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]

                if word not in words:
                    continue

                # 选择这个单词
                path.append(word)

                # 下一段从 end 开始
                dfs(end)

                # 撤回，尝试其他切法
                path.pop()

        dfs(0)
        return res