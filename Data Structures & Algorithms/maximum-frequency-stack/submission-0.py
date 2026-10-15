class FreqStack:

    def __init__(self):
        # 记录每个数字出现的次数
        self.freq = {}

        # key 是频率，value 是一个 Stack
        self.group = {}

        # 当前最大的频率
        self.maxFreq = 0

    def push(self, val: int) -> None:

        # 更新 val 的出现次数
        self.freq[val] = self.freq.get(val, 0) + 1

        # 得到 val 当前的频率
        f = self.freq[val]

        # 如果这个频率还没有对应的 Stack，就新建
        if f not in self.group:
            self.group[f] = []

        # 把 val 加入对应频率的 Stack
        self.group[f].append(val)

        # 更新当前最大频率
        self.maxFreq = max(self.maxFreq, f)

    def pop(self) -> int:

        # 从最高频率对应的 Stack 中弹出最近加入的元素
        val = self.group[self.maxFreq].pop()

        # 这个数字的出现次数减一
        self.freq[val] -= 1

        # 如果最高频率的 Stack 已经空了
        # 说明当前最大频率应该减一
        if not self.group[self.maxFreq]:
            self.maxFreq -= 1

        return val