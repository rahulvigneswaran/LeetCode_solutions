class Twitter:

    def __init__(self):
        self.time = 0
        self.followdict = defaultdict(set)
        self.feed = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.feed[userId].append((self.time, tweetId))
        self.time -= 1 # because we will be using maxheap

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        self.followdict[userId].add(userId)
        
        for user in self.followdict[userId]:
            index = len(self.feed[user]) - 1
            if index >= 0:
                time, tweetId = self.feed[user][index]
                heap.append((time, tweetId, user, index - 1))
        
        heapq.heapify(heap)
        res = []

        while heap and len(res) < 10:
            _, tweetId, user, index = heapq.heappop(heap)
            res.append(tweetId)

            if index >= 0:
                # take the next recent and push into heap
                time, tweetId = self.feed[user][index]
                heapq.heappush(heap, (time, tweetId, user, index - 1))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followdict[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followdict[followerId]:
            self.followdict[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)