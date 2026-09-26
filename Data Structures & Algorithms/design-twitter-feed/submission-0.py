import heapq

class Twitter:

    def __init__(self):
        self.following = {}
        self.post = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:

        if userId not in self.post:
            self.post[userId] = []

        self.post[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:

        heap = []

        # User + everyone they follow
        users = {userId}

        if userId in self.following:
            users.update(self.following[userId])

        for user in users:

            if user in self.post and self.post[user]:

                index = len(self.post[user]) - 1
                time, tweetId = self.post[user][index]

                heapq.heappush(
                    heap,
                    (-time, tweetId, user, index)
                )

        res = []

        while heap and len(res) < 10:

            time, tweetId, user, index = heapq.heappop(heap)

            res.append(tweetId)

            # Get previous tweet from same user
            if index > 0:

                index -= 1

                old_time, old_tweet = self.post[user][index]

                heapq.heappush(
                    heap,
                    (-old_time, old_tweet, user, index)
                )

        return res

    def follow(self, followerId: int, followeeId: int) -> None:

        if followerId not in self.following:
            self.following[followerId] = set()

        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:

        if followerId in self.following:
            self.following[followerId].discard(followeeId)