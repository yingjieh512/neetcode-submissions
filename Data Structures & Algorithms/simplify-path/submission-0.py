class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for part in path.split("/"):
            if part == "" or part == ".":
                continue

            elif part == "..":
                # 根目录不能再往上走
                if stack:
                    stack.pop()

            else:
                stack.append(part)

        # 用 / 连接目录名，再补上开头的 /
        return "/" + "/".join(stack)