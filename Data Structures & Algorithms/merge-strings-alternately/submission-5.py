class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
            a=0
            b=0
            res=[]
            while a < len(word1) or b < len(word2):
                if a==len(word1):
                    res.append(word2[b:])
                    return "".join(res)
                elif b==len(word2):
                    res.append(word1[a:])
                    return "".join(res)
                res.append(word1[a])
                res.append(word2[b])
                a+=1
                b+=1
            return "".join(res)