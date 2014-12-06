import json
import redis

__author__ = 'ubuntu'

import twitter
from TwitterCommunities.local_settings import *

class Compare():
    def __init__(self):
        self.api = twitter.Api(consumer_key=Consumer_Key_API_Key,
                      consumer_secret=Consumer_Secret_API_Secret,
                      access_token_key=Access_Token,
                      access_token_secret=Access_Token_Secret)
        self.r = redis.StrictRedis(host='localhost', port=6379, db=0)

# print pprint.pformat(api.VerifyCredentials().__dict__)

# print pprint.pformat(api.GetRateLimitStatus())

    def get_matches(self, user1, user2, allow_cached=True):
        cached = False

        u1_ids = self.r.get(user1 + '.following')
        if u1_ids is None or allow_cached == False:
            print 'redis missing ' + str(user1 + '.following')
            u1_ids = self.api.GetFriendIDs(screen_name=user1)
            self.r.set(user1 + '.' + 'following', json.dumps(u1_ids))
        else:
            cached = True
            u1_ids = json.loads(u1_ids)
            print 'redis had ' + str(len(u1_ids)) + ' for ' + user1

        u2_ids = self.r.get(user2 + '.following')
        if u2_ids is None or allow_cached == False:
            print 'redis missing ' + str(user2 + '.following')
            u2_ids = self.api.GetFriendIDs(screen_name=user2)
            self.r.set(user2 + '.' + 'following', json.dumps(u2_ids))
        else:
            cached = True
            u2_ids = json.loads(u2_ids)
            print 'redis had ' + str(len(u2_ids)) + ' for ' + user2

        commons = []
        for key in u1_ids:
            if key in u2_ids:
                commons.append(key)

        return u1_ids, u2_ids, commons, cached

    def get_follower_matches(self, user1, user2, allow_cached=True):
        cached = False

        u1_followed_by = self.r.get(user1 + '.followed')
        if u1_followed_by is None or allow_cached == False:
            print 'redis missing ' + str(user1 + '.followed')
            u1_followed_by = self.api.GetFollowerIDs(screen_name=user1)
            self.r.set(user1 + '.' + 'followed', json.dumps(u1_followed_by))
        else:
            cached = True
            u1_followed_by = json.loads(u1_followed_by)
            print 'redis had ' + str(len(u1_followed_by)) + ' for ' + user1

        u2_followed_by = self.r.get(user2 + '.followed')
        if u2_followed_by is None or allow_cached == False:
            print 'redis missing ' + str(user2 + '.followed')
            u2_followed_by = self.api.GetFollowerIDs(screen_name=user2)
            self.r.set(user2 + '.' + 'followed', json.dumps(u2_followed_by))
        else:
            cached = True
            u2_followed_by = json.loads(u2_followed_by)
            print 'redis had ' + str(len(u2_followed_by)) + ' for ' + user2

        commons_followed_by = []
        for key in u1_followed_by:
            if key in u2_followed_by:
                commons_followed_by.append(key)

        return u1_followed_by, u2_followed_by, commons_followed_by, cached

