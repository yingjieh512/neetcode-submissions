class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1  # 今天自己算一天

        while self.stack and self.stack[-1][0] <= price:
            old_price, old_span = self.stack.pop()
            span += old_span

        self.stack.append((price, span))
        return span