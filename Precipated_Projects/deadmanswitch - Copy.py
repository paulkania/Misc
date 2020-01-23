import tweepy
import datetime
import smtplib
from email.mime.text import MIMEText #used type:localhost
import ssl
import getpass
#http://docs.tweepy.org/en/v3.5.0/api.html
# https://developer.twitter.com/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-friends-list


tw_keys = {
        'ck'   :     'xjogzUgrFDzRSpDok7ONegctr',
        'cs'   :  'WRfRgUOFzfiMpInpAdu0OycexPCmXaFIjlLL9TyV4yb8v6Ut7O',
        'atk'   : '1188183335748689925-Cv4rODGb2RDuzigU3G3ZLM73Cax1nh',
        'ats' :'e4gH7WFFFSMB2VdKA14bGP3R866K1kxWRGWR5KmsCQDuC'}

auth = tweepy.OAuthHandler(tw_keys['ck'], tw_keys['cs'])
auth.set_access_token(tw_keys['atk'], tw_keys['ats'])
api = tweepy.API(auth)

most_recent_activity = api.user_timeline(count=1)
for tweet in most_recent_activity:
    tweet_time = tweet.created_at
    tweet_meat = tweet.text

print(tweet_meat)
api.update_status('hellowowlrdddd')


# current_time=datetime.datetime.utcnow()
# set_threshold_days = 4
# future_time_thresh = tweet_time+datetime.timedelta(days=set_threshold_days)
#
# threshold = future_time_thresh - current_time
# threshold = str(threshold)
# print('time until threshold',threshold,'------->',threshold[0])
#
# #ssl stuff
# #local message = MIMEText('are you OK? do you need more vespene gas?')
# msg = 'are you hurt, I notice you have not been active on twitter for {} days. \n do you need more vespene gas?'.format(set_threshold_days)
# frm = 'p.rozehnal@gmail.com'
# to = 'p.rozehnal@gmail.com'
# port =465
# cntxt = ssl.create_default_context()
# if threshold[0] == '-':
#     # pw= 'dontshowmypw'
#     pw = input('pwd plz') # x=getpass.getpass(prompt='papers plz')
#     with smtplib.SMTP_SSL("smtp.gmail.com",port,context=cntxt) as server:
#         server.login("p.rozehnal@gmail.com",pw)
#         server.sendmail(frm,to,msg)
#
#
#     # how do i run this program automatically? # run a bat file on startup//sleeup
