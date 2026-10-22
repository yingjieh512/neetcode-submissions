import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # 按原始开始时间处理，保证早来的会议优先
        meetings.sort()

        # 空闲房间堆：优先取编号最小的房间
        available = list(range(n))
        heapq.heapify(available)

        # 忙碌房间堆：(结束时间, 房间编号)
        # 先比较结束时间，再比较房间编号
        busy = []

        # 每个房间安排的会议数量
        count = [0] * n

        for start, end in meetings:
            duration = end - start

            # 把当前已经结束会议的房间全部释放
            while busy and busy[0][0] <= start:
                finish, room = heapq.heappop(busy)
                heapq.heappush(available, room)

            if available:
                # 有空房间：正常开始，选择编号最小的
                room = heapq.heappop(available)
                finish = end
            else:
                # 没有空房间：等待最早空出来的房间
                finish, room = heapq.heappop(busy)

                # 延期后仍保持原来的会议时长
                finish += duration

            count[room] += 1
            heapq.heappush(busy, (finish, room))

        # 从小编号开始，只在次数更多时更新，平局保留小编号
        answer = 0
        for room in range(1, n):
            if count[room] > count[answer]:
                answer = room

        return answer