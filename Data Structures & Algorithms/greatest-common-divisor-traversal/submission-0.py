class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n = len(nums)

        if n == 1:
            return True

        if 1 in nums:
            return False

        # 1. Union Find
        parent = list(range(n))
        size = [1] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            pa = find(a)
            pb = find(b)

            if pa == pb:
                return

            if size[pa] < size[pb]:
                pa, pb = pb, pa

            parent[pb] = pa
            size[pa] += size[pb]

        # 2. 预计算最小质因数
        m = max(nums)
        spf = list(range(m + 1))

        for i in range(2, int(m ** 0.5) + 1):
            if spf[i] == i:
                for j in range(i * i, m + 1, i):
                    if spf[j] == j:
                        spf[j] = i

        # 3. 用共同质因数连接节点
        prime_owner = {}

        for i, num in enumerate(nums):
            while num > 1:
                p = spf[num]

                if p in prime_owner:
                    union(i, prime_owner[p])
                else:
                    prime_owner[p] = i

                # 去掉当前质因数的所有次方
                while num % p == 0:
                    num //= p

        # 4. 判断是否全部连通
        root = find(0)

        for i in range(1, n):
            if find(i) != root:
                return False

        return True