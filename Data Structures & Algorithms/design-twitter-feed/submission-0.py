import heapq
from collections import defaultdict

class Twitter:
    def __init__(self):
        self.t = defaultdict(list)
        self.f = defaultdict(set)
        self.time = 0

    def postTweet(self, userId, tweetId):
        self.t[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId):
        h = []
        users = self.f[userId] | {userId}

        for u in users:
            if self.t[u]:
                i = len(self.t[u]) - 1
                time, tweet = self.t[u][i]
                heapq.heappush(h, (-time, u, i, tweet))

        ans = []
        while h and len(ans) < 10:
            _, u, i, tweet = heapq.heappop(h)
            ans.append(tweet)
            if i:
                i -= 1
                time, tweet = self.t[u][i]
                heapq.heappush(h, (-time, u, i, tweet))

        return ans

    def follow(self, followerId, followeeId):
        self.f[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        self.f[followerId].discard(followeeId)