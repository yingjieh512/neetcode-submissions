
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 所有加油站的总净收益
        # 用来判断整个环路是否有足够的汽油
        total = 0

        # 从当前候选起点出发，剩余的汽油
        tank = 0

        # 当前候选的起点
        start = 0

        # 遍历所有加油站
        for i in range(len(gas)):

            # 在当前站加油，并扣除前往下一站的消耗
            diff = gas[i] - cost[i]

            # 更新整个环路的净收益
            total += diff

            # 更新从当前候选起点出发的剩余汽油
            tank += diff

            # 如果油量变成负数
            # 说明从 start 出发无法经过当前站
            if tank < 0:

                # start 到 i 之间的所有站点
                # 都不可能是有效起点
                # 因此直接从 i+1 重新尝试
                start = i + 1

                # 新的起点从空油箱开始
                tank = 0

        # 如果整个环路的总汽油小于总消耗
        # 无论从哪里出发，都不可能完成一圈
        if total < 0:
            return -1

        # 总汽油足够时，贪心算法找到的起点有效
        return start
