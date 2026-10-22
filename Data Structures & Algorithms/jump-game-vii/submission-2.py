from collections import deque

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        q = deque([0])
        visited = set([0])

        while q:
            i = q.popleft()

            if i == n - 1:
                return True

            for j in range(i + minJump, min(i + maxJump, n - 1) + 1):
                if s[j] == "0" and j not in visited:
                    q.append(j)
                    visited.add(j)

        return False