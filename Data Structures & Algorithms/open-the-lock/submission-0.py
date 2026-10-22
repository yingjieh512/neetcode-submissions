from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)

        if "0000" in dead:
            return -1

        queue = deque([("0000", 0)])
        visited = {"0000"}

        while queue:
            code, steps = queue.popleft()

            if code == target:
                return steps

            # 选择转动哪一个轮子
            for i in range(4):
                digit = int(code[i])

                # 这个轮子向前或向后转一格
                for change in (-1, 1):
                    new_digit = (digit + change) % 10

                    # 只替换第 i 个字符，其他字符保持不变
                    new_code = (
                        code[:i] + str(new_digit) + code[i + 1:]
                    )

                    if new_code in dead or new_code in visited:
                        continue

                    # 入队时就标记，避免重复入队
                    visited.add(new_code)
                    queue.append((new_code, steps + 1))

        return -1