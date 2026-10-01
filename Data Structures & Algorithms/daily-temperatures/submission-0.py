from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):

            while stack and temp > stack[-1][0]:
                old_temp, old_i = stack.pop()
                result[old_i] = i - old_i

            stack.append((temp, i))

        return result