class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = sorted(s1)
        n = len(s1)

        for i in range(len(s2) - n + 1):
            if sorted(s2[i:i+n]) == target:
                return True

        return False