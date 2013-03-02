tweetText = "5:2 3:1 4:5 5/2 5-2 5:2"
#tweetText = "5-2"
searchScore = ""
runningTotal={}
ii=0
for i in listAllPerms[0]:
	searchScore = ''.join(listAllPerms[0][ii])
	if tweetText.count(searchScore)==1:
		runningTotal[searchScore]=runningTotal[searchScore]+1
	ii=ii+1