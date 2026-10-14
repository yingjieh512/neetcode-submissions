
from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        # 如果总牌数不能被 groupSize 整除，
        # 就不可能把所有牌分成大小相同的组
        if len(hand) % groupSize != 0:
            return False

        # 从小到大排序
        # 保证我们每次从剩余的最小数字开始组顺子
        hand.sort()

        # 统计每个数字还剩多少张牌
        count = Counter(hand)

        # 按从小到大的顺序尝试每个数字
        for num in hand:

            # 当前数字已经全部用完
            # 不需要再从它开始组新的顺子
            if count[num] == 0:
                continue

            # 当前 num 是剩余牌中最小的数字
            # 必须从 num 开始构建长度为 groupSize 的顺子
            for card in range(num, num + groupSize):

                # 如果缺少任何一张必须的牌
                # 就不可能完成分组
                if count[card] == 0:
                    return False

                # 使用一张当前数字的牌
                count[card] -= 1

        # 所有牌都成功分组
        return True
