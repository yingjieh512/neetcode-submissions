
class Solution:
    def checkValidString(self, s: str) -> bool:
        # low：可能剩余的未匹配左括号数量的最小值
        # high：可能剩余的未匹配左括号数量的最大值
        low = 0
        high = 0

        for c in s:

            if c == '(':
                # 必须增加一个未匹配左括号
                low += 1
                high += 1

            elif c == ')':
                # 必须消耗一个左括号
                low -= 1
                high -= 1

            else:
                # 当前是 *
                # 最少：当作右括号，消耗一个左括号
                low -= 1

                # 最多：当作左括号，增加一个左括号
                high += 1

            # 连最大可能值都小于 0
            # 说明右括号已经太多，必然不合法
            if high < 0:
                return False

            # 最小未匹配数量不能为负数
            # 可以通过让 * 充当空字符来保持 0
            low = max(0, low)

        # 存在一种分配方式，让所有左括号被匹配
        return low == 0
