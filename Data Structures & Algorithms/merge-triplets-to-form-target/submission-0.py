
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        # found[i] 表示：
        # 是否已经找到一个合法 triplet，
        # 它在第 i 个位置上的值等于 target[i]
        found = [False, False, False]

        # 遍历所有 triplet
        for a, b, c in triplets:

            # 如果任何一个数字超过 target 对应位置
            # 这个 triplet 就不能参与合并
            # 因为 max() 只会让数字变大，不会变小
            if a > target[0] or b > target[1] or c > target[2]:
                continue

            # 当前 triplet 是合法的
            # 检查它可以提供哪些目标数字
            if a == target[0]:
                found[0] = True

            if b == target[1]:
                found[1] = True

            if c == target[2]:
                found[2] = True

        # 如果三个位置都能够达到 target
        # 就能通过合并得到目标 triplet
        return all(found)
