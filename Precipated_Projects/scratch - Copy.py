################localhost
#python -m smtpd -c DebuggingServer -n localhost:1020 or 4000 or 8000 or 8080
import tweepy
import datetime
import smtplib
from email.mime.text import MIMEText #used type:localhost
import ssl
import getpass
#Add your credentials here
tw_keys = {
        'ck'   :     'xfF7gFq6XT52DswRRP3ANOFAb',
        'cs'   :  '2zrHKTHQeE0ejaMyXb5AvjetlCMdQ6wjlBx9edVnngTw53c9bG'}

#Setup access to API
auth = tweepy.OAuthHandler(tw_keys['ck'], tw_keys['cs'])
# auth.set_access_token(tw_keys['atk'], tw_keys['ats'])
api = tweepy.API(auth)

most_recent_activity = api.user_timeline(id=21519885, count=3)
#https://codeofaninja.com/tools/find-twitter-id
#http://docs.tweepy.org/en/v3.5.0/api.html
#blockstream_team
#@BlockstreamT

#https://developer.twitter.com/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-friends-list
# API.user_timeline([id/user_id/screen_name][, since_id][, max_id][, count][, page])

for tweet in most_recent_activity:
    tweet_time = tweet.created_at
    tweet_meat = tweet.text
    tweet_user = tweet.user.screen_name
    print(tweet_time,tweet_meat,tweet_user)
# api.update_status(tweet_meat)

#     # how do i run this program automatically? # run a bat file on startup//sleeup
