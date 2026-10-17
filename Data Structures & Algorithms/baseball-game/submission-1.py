class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for i in range(len(operations)):

            if operations[i] == "+":
                # 将前两次有效得分相加，作为新的一次得分
                a = stack[-1]
                b = stack[-2]
                sumab = a + b
                stack.append(sumab)

            elif operations[i] == "D":
                # 上一次有效得分的两倍
                newnum = stack[-1] * 2
                stack.append(newnum)

            elif operations[i] == "C":
                # 取消上一次有效得分
                stack.pop()

            else:
                # 普通数字，转换为整数后加入栈
                stack.append(int(operations[i]))

        # 返回所有有效得分的总和
        return sum(stack)