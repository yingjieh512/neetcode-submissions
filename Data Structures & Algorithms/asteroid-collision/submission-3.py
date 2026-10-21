class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for i in range(len(asteroids)):
            if asteroids[i]>0:
                stack.append(asteroids[i])
            else:
                # 当前负数消灭所有比它小的正数
                while stack and stack[-1] > 0 and stack[-1] < abs(asteroids[i]):
                    stack.pop()

                # 大小相等，两个都消失
                if stack and stack[-1] == abs(asteroids[i]):
                    stack.pop()

                # 没有正数阻挡，当前负数存活
                elif not stack or stack[-1] < 0:
                    stack.append(asteroids[i])
        return stack