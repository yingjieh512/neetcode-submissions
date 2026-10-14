class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num = 0

        for ch in s:

            # 如果遇到数字，记录重复次数
            # 例如 "12" 需要解析成整数 12
            if ch.isdigit():
                num = num * 10 + int(ch)

            # 遇到左括号，把重复次数和括号入栈
            elif ch == "[":
                stack.append(num)
                stack.append("[")
                num = 0

            # 遇到右括号，开始解码当前这一层
            elif ch == "]":
                temp = []

                # 一直弹出，直到找到对应的左括号
                while stack[-1] != "[":
                    temp.append(stack.pop())

                # 删除左括号
                stack.pop()

                # 取出重复次数
                times = stack.pop()

                # 因为 Stack 是后进先出
                # 所以需要 reverse，还原字符顺序
                substring = "".join(reversed(temp))

                # 重复 times 次，再放回 Stack
                stack.append(substring * times)

            else:
                # 普通字母直接入栈
                stack.append(ch)

        # 把 Stack 里剩余字符串拼接起来
        return "".join(stack)