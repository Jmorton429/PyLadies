########
# Before you do this, paste following command into your terminal:
# export TWITTER_CONS_KEY='Your Consumer Key'
# export TWITTER_CONS_SECRET='Your Consumer Secret'
# export TWITTER_ACCESS_TOKEN='Your Access Token'
# export TWITTER_ACCESS_SECRET='Your Access Secret'
########

import os
import twitter

consumer_key = os.environ['TWITTER_CONS_KEY']
consumer_secret = os.environ['TWITTER_CONS_SECRET']
access_token = os.environ['TWITTER_ACCESS_TOKEN']
access_token_secret = os.environ['TWITTER_ACCESS_SECRET']

api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_token,
                  access_token_secret=access_token_secret)

print api.VerifyCredentials()
print ""
statuses = api.GetUserTimeline()
print [s.text for s in statuses]
print ""
print "I tweeted \"" + statuses[0].text + "\" at " + statuses[0].user_mentions[0].name + " (@" + statuses[0].user_mentions[0].screen_name + ")."
