from collections import defaultdict, OrderedDict

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity

        # key -> (value, frequency)
        self.key_info = {}

        # frequency -> ordered keys
        self.freq_map = defaultdict(OrderedDict)

        self.min_freq = 0

    def update_freq(self, key):
        value, freq = self.key_info[key]

        # 从旧频率组删除
        del self.freq_map[freq][key]

        # 如果旧组为空
        if not self.freq_map[freq]:
            del self.freq_map[freq]

            if self.min_freq == freq:
                self.min_freq += 1

        # 加入新频率组
        self.freq_map[freq + 1][key] = None

        self.key_info[key] = (value, freq + 1)

    def get(self, key: int) -> int:
        if key not in self.key_info:
            return -1

        value, freq = self.key_info[key]

        self.update_freq(key)

        return value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        # key 已存在：更新 value，并增加频率
        if key in self.key_info:
            _, freq = self.key_info[key]
            self.key_info[key] = (value, freq)
            self.update_freq(key)
            return

        # 容量满了：淘汰 LFU，相同时淘汰 LRU
        if len(self.key_info) == self.capacity:
            old_key, _ = self.freq_map[self.min_freq].popitem(last=False)

            del self.key_info[old_key]

            if not self.freq_map[self.min_freq]:
                del self.freq_map[self.min_freq]

        # 插入新 key，频率初始化为 1
        self.key_info[key] = (value, 1)
        self.freq_map[1][key] = None

        self.min_freq = 1