class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)
        res=[]
        path=[]
        def dfs(start):
            if start==len(s):
                res.append(" ".join(path))
                return
            for end in range(start+1,len(s)+1):
                string=s[start:end]
                if string not in words:
                    continue
                
                path.append(string)
                dfs(end)
                path.pop()


        dfs(0)
        return res