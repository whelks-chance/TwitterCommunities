__author__ = 'ubuntu'

import twitter
from TwitterCommunities.local_settings import *

class Compare():
    def __init__(self):
        self.api = twitter.Api(consumer_key=Consumer_Key_API_Key,
                      consumer_secret=Consumer_Secret_API_Secret,
                      access_token_key=Access_Token,
                      access_token_secret=Access_Token_Secret)

# print pprint.pformat(api.VerifyCredentials().__dict__)

# print pprint.pformat(api.GetRateLimitStatus())

    def get_matches(self, user1, user2):
        u1_ids = self.api.GetFriendIDs(screen_name=user1)

        u2_ids = self.api.GetFriendIDs(screen_name=user2)

        commons = []
        for key in u1_ids:
            if key in u2_ids:
                commons.append(key)

        return u1_ids, u2_ids, commons

    def get_follower_matches(self, user1, user2):
        u1_followed_by = self.api.GetFollowerIDs(screen_name=user1)

        u2_followed_by = self.api.GetFollowerIDs(screen_name=user2)

        commons_followed_by = []
        for key in u1_followed_by:
            if key in u2_followed_by:
                commons_followed_by.append(key)

        return u1_followed_by, u2_followed_by, commons_followed_by

