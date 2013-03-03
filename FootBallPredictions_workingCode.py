#set up API call

from urllib import urlopen
from urllib import urlencode


#create a url to look for the last 500 search results in english with #thfcvafc and "prediction" 

prefix = "http://search.twitter.com/search.json"
suffix = "?"+ urlencode({"q":"#thfcvafc+prediction","rpp":500,"result_type":"recent","lang":"en"})
url = prefix+suffix

#read the data

data = urlopen(url).read()
from json import loads
response = loads(data)
tweets = response["results"] 

#isolate the text of the tweets from the data

tweetlist = []

for t in tweets:
  if t["text"]:
    tweetText = t["text"]
    tweetlist.append(str(tweetText))
longString=""
for i in tweetlist:
  longString=longString+i

#normalize all the formats of score predictions
cleanStringCln = longString.replace(":","-")
cleanStringSlash=cleanStringCln.replace("/","-")
cleanString1 = cleanStringSlash.replace(" -","-")
cleanString2 = cleanString1.replace("- ","-")

finalString=cleanString2


list2Perm = ["0","1","2","3","4","5","6","7","8","9","10"]
listPerm = [a+"-"+b
            for a in list2Perm
            for b in list2Perm
            ]
listAllPerms=[listPerm]



#set up empty containers
searchScore = ""
runningTotal={}
numberOfPredictions=0
ii=0
#count the number of times a score occurs, add it to a dictionary, update the number of predictions
for i in listAllPerms[0]:
	searchScore = ''.join(listAllPerms[0][ii])
	if finalString.count(searchScore) > 0:
		runningTotal[searchScore]=finalString.count(searchScore)
		numberOfPredictions=numberOfPredictions+finalString.count(searchScore)
	ii=ii+1
print runningTotal
print numberOfPredictions



