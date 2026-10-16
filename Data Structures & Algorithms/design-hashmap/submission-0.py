class MyHashMap:

    def __init__(self):
        self.myhash = {}

    def put(self, key: int, value: int) -> None:
        # 插入或更新 key 对应的 value
        self.myhash[key] = value

    def get(self, key: int) -> int:
        # 如果 key 不存在，返回 -1
        return self.myhash.get(key, -1)

    def remove(self, key: int) -> None:
        # 如果 key 存在就删除，不存在也不会报错
        self.myhash.pop(key, None)