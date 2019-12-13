#
# @lc app=leetcode id=355 lang=python3
#
# [355] Design Twitter
#

# @lc code=start


class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.followShip = []
        self.post = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.post.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        res = []
        count = 0
        for i in range(len(self.post))[::-1]:
            if self.post[i][0] == userId or (userId, self.post[i][0]) in self.followShip:
                res.append(self.post[i][1])
                count += 1
                if count == 10:
                    break
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        ship = (followerId, followeeId)
        if ship not in self.followShip:
            self.followShip.append(ship)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        ship = (followerId, followeeId)
        if ship in self.followShip:
            self.followShip.remove(ship)
# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
# @lc code=end

# Time Limit Exceeded
# 22/23 cases passed(N/A)
