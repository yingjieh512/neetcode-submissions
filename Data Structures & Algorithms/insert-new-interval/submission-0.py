class Solution:
    def insert(self, intervals, newInterval):
        result = []

        start, end = newInterval

        for s, e in intervals:

            # 当前 interval 在 newInterval 左边
            if e < start:
                result.append([s, e])

            # 当前 interval 在 newInterval 右边
            elif end < s:
                result.append([start, end])

                # 后面的都不用再 merge 了
                start, end = s, e

            # overlap
            else:
                start = min(start, s)
                end = max(end, e)

        result.append([start, end])

        return result