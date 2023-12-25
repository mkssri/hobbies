import datetime
class Twitter:

    def __init__(self):
        self.store = collections.defaultdict(list)
        self.friends = collections.defaultdict(list)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        ep = datetime.datetime(1970,1,1,0,0,0)
        x = (datetime.datetime.utcnow()- ep).total_seconds()
        self.store[userId].append((-x, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:

        def addTweets(min_heap, tweets):
            for tweet in tweets:
                heapq.heappush(min_heap, tweet)
            return min_heap

        min_heap, res = [], []
        heapq.heapify(min_heap)

        min_heap= addTweets(min_heap,self.store[userId])

        for user in self.friends[userId]:
            min_heap= addTweets(min_heap,self.store[user])


        for i in range(10):
            if len(min_heap)>0:
                res.append(heapq.heappop(min_heap)[1])
        
        return res
        
        
    def follow(self, followerId: int, followeeId: int) -> None:
        if(followeeId not in self.friends[followerId]):
            self.friends[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:

        followers = self.friends[followerId]
        n = len(followers)

        for i in range(n):
            if followers[i]==followeeId:
                followers.pop(i)
                break
        
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)