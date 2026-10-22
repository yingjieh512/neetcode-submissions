from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)

        r = deque()
        d = deque()

        for i in range(n):
            if senate[i] == "R":
                r.append(i)
            else:
                d.append(i)

        while r and d:
            ri = r.popleft()
            di = d.popleft()

            if ri < di:
                r.append(ri + n)
            else:
                d.append(di + n)

        if r:
            return "Radiant"
        else:
            return "Dire"