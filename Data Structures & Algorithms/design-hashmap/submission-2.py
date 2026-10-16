class MyHashMap:

    def __init__(self):
        # 创建 1009 个 bucket
        # 每个 bucket 都是一个独立的 list
        self.size = 1009
        self.buckets = [[] for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        # 第一步：计算 key 应该在哪个 bucket
        index = key % self.size

        # 第二步：找到对应的 bucket
        bucket = self.buckets[index]

        # 第三步：检查 key 是否已经存在
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                # key 存在：更新它对应的 value
                bucket[i] = (key, value)
                return

        # key 不存在：插入新的 key-value pair
        bucket.append((key, value))

    def get(self, key: int) -> int:
        # 第一步：计算 bucket index
        index = key % self.size
        bucket = self.buckets[index]

        # 第二步：遍历 bucket，找到对应的 key
        for k, v in bucket:
            if k == key:
                return v

        # 找不到 key，返回 -1
        return -1

    def remove(self, key: int) -> None:
        # 第一步：计算 bucket index
        index = key % self.size
        bucket = self.buckets[index]

        # 第二步：查找 key 所在的位置
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                # 找到后删除对应的 key-value pair
                bucket.pop(i)
                return