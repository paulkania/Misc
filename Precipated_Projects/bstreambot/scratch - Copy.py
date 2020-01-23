import tweepy
import pickle
import os

##get to correct wd to load pickled document
os.chdir(r"C:\Users\proze\Documents\GitHub\Euler-2019\Precipated_Projects\bstreambot") #desktop
print(os.getcwd(),'<--current directory') #prints current directory to ensure you're in the right folder

#Load the pickle file
with open("Users_ID.txt", "rb") as myFile:
    team_by_since_id = pickle.load(myFile)
print('top',team_by_since_id)
print('top',team_by_since_id['pwuille'])

##load pickled keys.
with open("tw_keys.txt", "rb") as myFile:
    tw_keys = pickle.load(myFile)

##Setup access to API
auth = tweepy.OAuthHandler(tw_keys['ck'], tw_keys['cs'])
auth.set_access_token(tw_keys['atk'], tw_keys['ats'])
api = tweepy.API(auth)

pwuille = api.user_timeline(screen_name='pwuille', count=50,since_id=team_by_since_id['pwuille']-1)
adam3us = api.user_timeline(screen_name='adam3us', count=50,since_id=team_by_since_id['adam3us']-1)
Mario_Gibney = api.user_timeline(screen_name='mario_gibney', count=60,since_id=team_by_since_id['Mario_Gibney']-1)

team = [pwuille,Mario_Gibney,adam3us]

print('\n','\n','\n')
for user in team: # user is type 'ResultSet'
    print('new user')
    for tweet in user:  # tweet is type 'Status'
        # print(111, tweet.text[0:2],tweet.author.screen_name, tweet.text, tweet.text[0:2],'<--0to2', tweet.in_reply_to_screen_name)
        if tweet.text[0:2] != 'RT' and tweet.in_reply_to_screen_name is None:
            # print('output',tweet.author.screen_name,team_by_since_id[str(tweet.author.screen_name)],tweet.text)
            team_by_since_id[str(tweet.author.screen_name)] =  tweet.id
            api.retweet(tweet.id)

print(team_by_since_id)
    
## save AKA dump user dictionary
with open("Users_ID.txt", "wb") as myFile:
    pickle.dump(team_by_since_id, myFile)

#Load the pickle file
with open("Users_ID.txt", "rb") as myFile:
    team_by_since_id = pickle.load(myFile)
print('bottom',team_by_since_id)
print('bottom',team_by_since_id['pwuille'])

