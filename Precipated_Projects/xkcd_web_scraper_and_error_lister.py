import requests
from PIL import Image
from bs4 import BeautifulSoup
import io


def getsoup(aurl):
	source_code = requests.get(aurl)
	text = source_code.text
	soup =  BeautifulSoup(text,'html.parser')
	return soup

#part 1 - finding the most recent entry (as an integer)
headurl = 'https://xkcd.com/'
headsoup = getsoup(headurl)
x = str(headsoup.find('meta',{'property':'og:url'})).split('/')
headpage = int()
for datum in x:
	if datum.isnumeric():
		headpage = int(datum)
		break
##########end part1

headpage = 2255 #2255
while headpage > 0:
	currenturl = headurl+str((headpage))
	currentsoup = getsoup(currenturl)
	if str(currentsoup.find('meta',{'property':'og:image'})).split(('"')) == ['None']:
		headpage -= 1 #can also easily append this headpage to an error list, to see which ones got the axe.
		continue
	elif str(currentsoup.find('meta',{'property':'og:image'})).split(('"'))[1][-3:] != 'png':
		x = str(currentsoup.find('meta',{'property':'og:image'})).split(('"'))[1]
	elif str(currentsoup.find('meta',{'property':'og:image'})).split(('"'))[1][-3:] != 'png': #or simply 'else' but i like to be explicit
		imgtags = currentsoup.findAll('img')
		for image in imgtags:
			if image['src'][:23] == '//imgs.xkcd.com/comics/':
				x='https:'+image['src']
				break #regression test this line added post-download.
	pull = requests.get(x)
	image = Image.open(io.BytesIO(pull.content))
	filepath = r"C:\Users\proze\Desktop\xkcd_dump1\""
	filename = str(headpage)+'.png'
	image.save(filepath[0:-1]+filename,format="png")
	print('saved',filepath[0:-1]+filename)
	headpage -=1

##############################
##############################
##############################
##############################
########error_lister_below...it's pretty much trash but im saving it anyways...


#include definitions and imports from above
errort1=[]
errort2=[]
def txtsaver(title,yourdict_or_list):
    with open(title, mode="w", encoding="iso-8859-1") as f:
        for place, item in enumerate(yourdict_or_list):
            f.write('%s\n' % item)
            if (place+1)%4==0:
                f.write('\n')
headpage = 2255 #root == 2255
while headpage > 0:
	print(headpage)
	currenturl = headurl+str((headpage))
	currentsoup = getsoup(currenturl)
	try:
		x = str(currentsoup.find('meta',{'property':'og:image'})).split(('"'))[1]
	except:
		errort1.append(headpage)
		headpage -= 1
		continue
	pull = requests.get(x)
	try: #xkcd2202 is a dead link
		image = Image.open(io.BytesIO(pull.content))
	except:
		errort2.append(headpage)
		headpage-=1
		continue
	headpage -= 1

txtsaver('error1.txt',errort1)
txtsaver('error2.txt',errort2)
# 	filepath = r"C:\Users\proze\Desktop\xkcd_dump\""
# 	filename = str(headpage)+'.png'
# 	#im.save(path+'/'+name)
# 	image.save(filepath[0:-1]+filename,   format="png")
# 	print('saved',filepath[0:-1]+filename)
# 	headpage -=1

