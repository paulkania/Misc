#README
#in order to add a new member to the list
#add 'username' to team of bstream file
#take minimum idstring and add it in form: team_since_id_dict['zackvoell']=x[0]

#if you accidentally run this program, thereby going back in time on a user's most recent dates,
# just run bstream without the (retweet api line) to get back to the most current post_id's


import pickle
import os

##get to correct wd, and load pickled dict.
os.chdir(r"C:\Users\proze\Documents\GitHub\Euler-2019\Precipated_Projects\bstreambot") #desktop
print(os.getcwd(),'<--current directory') #prints current directory to ensure you're in the right folder
with open("Users_ID.txt", "rb") as myFile:
    team_since_id_dict = pickle.load(myFile)
print('top',len(team_since_id_dict),team_since_id_dict)

#find a good starting id to impregnate the new user value...
_min=[]
for key,value in team_since_id_dict.items():
    _min.append(value)
    # print(key,type(key),value)
x=sorted(_min)
# print(x)
print('--->',x[0])


###uncomment out the line (safety's on sort of thing)
# team_since_id_dict['zackvoell']=x[0]
print('added',len(team_since_id_dict),team_since_id_dict)

#save new pickled dict.
with open("Users_ID.txt", "wb") as myFile:
    pickle.dump(team_since_id_dict, myFile)

