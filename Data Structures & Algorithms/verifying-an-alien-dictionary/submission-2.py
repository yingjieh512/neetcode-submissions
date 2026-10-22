class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        rank = {char: i for i, char in enumerate(order)}
        for i in range(len(words)-1):
            a, b = words[i], words[i + 1] 
            for j in range(min(len(a), len(b))):
                if a[j] == b[j]:
                    continue

                if rank[a[j]] > rank[b[j]]:
                    return False

                # 第一处不同：a 的字母更小，这一对顺序正确
                break
            else:
                # 比较范围内全部相同，检查长单词是否在前
                if len(a) > len(b):
                    return False
        return True
        