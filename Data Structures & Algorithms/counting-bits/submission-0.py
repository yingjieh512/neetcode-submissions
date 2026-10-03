class Solution:
    def countBits(self, n: int) -> List[int]:
        def hammingWeight(x):
            count = 0
            while x:
                count += x & 1
                x >>= 1
            return count

        result = []

        for i in range(n + 1):
            result.append(hammingWeight(i))

        return result