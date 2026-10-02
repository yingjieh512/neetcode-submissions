class Solution:
    from math import ceil
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            k = (left + right) // 2

            hours = 0
            for p in piles:
                hours += math.ceil(p/k)

            if hours <= h:
                # k 可以，但可能还能更小
                right = k
            else:
                # k 太小了，必须增大
                left = k + 1

        return left