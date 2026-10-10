from collections import defaultdict
import heapq
from typing import List

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        res = []

        # 自己 + 关注的人
        users = self.following[userId] | {userId}

        # 每人先放入最新的一条推文
        for user in users:
            if self.tweets[user]:
                idx = len(self.tweets[user]) - 1
                time, tweetId = self.tweets[user][idx]

                heap.append((-time, tweetId, user, idx))

        heapq.heapify(heap)

        # 取出最新的最多 10 条推文
        while heap and len(res) < 10:
            negTime, tweetId, user, idx = heapq.heappop(heap)

            res.append(tweetId)

            # 如果这个用户还有更旧的推文，放入 heap
            if idx > 0:
                time, nextTweet = self.tweets[user][idx - 1]

                heapq.heappush(
                    heap,
                    (-time, nextTweet, user, idx - 1)
                )

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)