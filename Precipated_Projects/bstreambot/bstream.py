#readme -
# impregnate 3 things:
#   1use definition A, (PAIR)
#   2turn off api.retweet, (SINGLE)
#   3impregnate dict without constraits, (SINGLE)
#   each of these is is a comment off/on singally (S), or in a vice-versa Pair (P)
#   a properly impregnated dict will have teh same length as the team list (16 as of writing)

#jan 24 test - most recent RT is Wuille's 'how should we call the roaring 20's/
#1
#there may have t be some fixing in regards to putting in a break after a api.retweet...but we'll see about that, just
#a hunch due to what i saw from manifold...where old tweets move 1 at a time...not sure why his lasted so many program runs//post-impregnation runs...
#we'll see tomorrow
#cheers, -january 23
#2 may have to try: retweet, except:print('youve already retweeted that)...but not probable since the impregnation technique seems solid.


import tweepy
import pickle
import os

##get to correct wd to load pickled document
os.chdir(r"C:\Users\proze\Documents\GitHub\Euler-2019\Precipated_Projects\bstreambot") #desktop
print(os.getcwd(),'<--current directory') #prints current directory to ensure you're in the right folder

#Load the pickle file
with open("Users_ID.txt", "rb") as myFile:
    team_since_id_dict = pickle.load(myFile)
print('top',team_since_id_dict)
print('top',len(team_since_id_dict))

##load pickled keys.
with open("tw_keys.txt", "rb") as myFile:
    tw_keys = pickle.load(myFile)

##Setup access to API
auth = tweepy.OAuthHandler(tw_keys['ck'], tw_keys['cs'])
auth.set_access_token(tw_keys['atk'], tw_keys['ats'])
api = tweepy.API(auth)

team = ['zackvoell','pwuille','Mario_Gibney','adam3us','wtogami','tomatodread','Excellion','jb55','n1ckler','Snyke','LarryBitcoin','notgrubles','humanifold','AlyseKilleen','SeleneJin','afilini','sanket1729']
print('team length -->',len(team))
# team = ['pwuille','Mario_Gibney','adam3us','wtogami','tomatodread','Excellion','jb55','n1ckler','Snyke',LarryBitcoin,notgrubles,humanifold,AlyseKilleen,SeleneJin,afilini,sanket1729]

def user_timeline(ateamlist,acount):
    __teamoutput = []
    for aname in ateamlist:
        try:
            aname = api.user_timeline(screen_name=str(aname), count=acount, since_id=team_since_id_dict[str(aname)])
            __teamoutput.append(aname)
        except tweepy.TweepError as e:
            print(aname,'blocked you, it is ok, dont take it personal paulo')
            continue
    return __teamoutput

def user_timeline_impregnation(ateamlist,acount,asince_last_post_id): #num ex1->12204185514351370U25
    _teamoutput=[]
    for aname in ateamlist:
        aname = api.user_timeline(screen_name=str(aname), count=acount, since_id=int(asince_last_post_id))
        _teamoutput.append(aname)
    return _teamoutput

# teamoutput = user_timeline_impregnation(team,40,1220418551435137) #on to impregnate, off if impregnated.
teamoutput = user_timeline(team,10) #off to impregnate, on if impregnated.



def retweet():
    i=0
    for member in teamoutput:
        i+=1
        for tweet in member:
            # team_since_id_dict[str(tweet.author.screen_name)] = tweet.id #on to impregnate, off if impregnated.
            if tweet.text[0:2] != 'RT' and tweet.in_reply_to_screen_name is None:
                print(i,tweet.author.screen_name,tweet.text)
                team_since_id_dict[str(tweet.author.screen_name)] =  tweet.id
                api.retweet(tweet.id)

    with open("Users_ID.txt", "wb") as myFile:
        pickle.dump(team_since_id_dict, myFile)

    print('bottom',len(team_since_id_dict),team_since_id_dict)
    # api.update_status('test003')
    return

#call the function so the bat script will execute.
retweet()



# pwuille = api.user_timeline(screen_name='pwuille', count=50,since_id=team_by_since_id['pwuille'])
# Mario_Gibney = api.user_timeline(screen_name='mario_gibney', count=60,since_id=team_by_since_id['Mario_Gibney'])
# adam3us = api.user_timeline(screen_name='adam3us', count=50,since_id=team_by_since_id['adam3us'])
# wtogami = api.user_timeline(screen_name='wtogami', count=50,since_id=team_by_since_id['wtogami'])
# tomatodread = api.user_timeline(screen_name='tomatodread', count=50,since_id=team_by_since_id['tomatodread'])
# excellion = api.user_timeline(screen_name='excellion', count=50,since_id=team_by_since_id['excellion'])
# jb55 = api.user_timeline(screen_name='jb55', count=50,since_id=team_by_since_id['jb55'])
# n1ckler = api.user_timeline(screen_name='n1ckler', count=50,since_id=team_by_since_id['n1ckler'])
# Snyke = api.user_timeline(screen_name='Snyke', count=50,since_id=team_by_since_id['Snyke'])
# LarryBitcoin = api.user_timeline(screen_name='LarryBitcoin', count=50,since_id=team_by_since_id['LarryBitcoin'])
# notgrubles = api.user_timeline(screen_name='notgrubles', count=50,since_id=team_by_since_id['notgrubles'])
# humanifold = api.user_timeline(screen_name='humanifold', count=50,since_id=team_by_since_id['humanifold'])
# AlyseKilleen = api.user_timeline(screen_name='AlyseKilleen', count=50,since_id=team_by_since_id['AlyseKilleen'])
# SeleneJin = api.user_timeline(screen_name='SeleneJin', count=50,since_id=team_by_since_id['SeleneJin'])
# afilini = api.user_timeline(screen_name='afilini', count=50,since_id=team_by_since_id['afilini'])
# sanket1729 = api.user_timeline(screen_name='sanket1729', count=50,since_id=team_by_since_id['sanket1729'])




# print('\n','\n')
# for user in team: # user is type 'ResultSet'
#     print('new user')
#     for tweet in user:  # tweet is type 'Status'
#         print(111,tweet.id, tweet, tweet.text[0:2],tweet.author.screen_name, tweet.text, tweet.text[0:2],'<--0to2', tweet.in_reply_to_screen_name)
#         if tweet.text[0:2] != 'RT' and tweet.in_reply_to_screen_name is None:
#             # print('output',tweet.author.screen_name,team_by_since_id[str(tweet.author.screen_name)],tweet.text)
#             team_by_since_id[str(tweet.author.screen_name)] =  tweet.id
#             # api.retweet(tweet.id)
#
# print(team_by_since_id)
#
# ## save AKA dump user dictionary
# with open("Users_ID.txt", "wb") as myFile:
#     pickle.dump(team_by_since_id, myFile)
#
# #Load the pickle file
# with open("Users_ID.txt", "rb") as myFile:
#     team_by_since_id = pickle.load(myFile)
# print('bottom',team_by_since_id)
# print('bottom',team_by_since_id['pwuille'])
#
