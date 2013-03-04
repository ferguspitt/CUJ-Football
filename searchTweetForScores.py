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
