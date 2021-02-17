import random

myList=[]
swList = []
aList = []
"""
def printDash(keyword, letter=""):
	#line = x
	line = ""
	for x in keyword:
		if letter==x:
			line += x
		else:
			line += "-"
		xline = line
	return xline
"""

def storageSW(sw):
	for x in sw:
		swList.append(x)
		aList.append("-")


def answerList(sw, answ):
	for x in range(0,len(sw)):
		if sw[x] == answ:
			aList[x] = answ
	w = ""
	for x in aList:
		w += x
	#print(w)
	return w 


xDic = {0:"python", 
		1:"computer",
		2:"keyboard",
		3:"internet",
		4:"mouse",
		}

secretId = random.randint(0,len(xDic)-1)
secretWord = xDic[secretId]
storageSW(secretWord) #rand kelime belli olduktan sonra kayır ediyor

print(answerList(secretWord,""))
counter = 0
while True:
	i = str(input("your guess: "))
	counter += 1
	q = answerList(secretWord, i)
	print(q)
	if q == secretWord:
		print("!!!{secret}!!!, try:{c}".format(c=counter,secret=secretWord))
		break

"""
answerList(secretWord,"o")
answerList(secretWord,"u")
answerList(secretWord,"m")
"""

#print(secretWord)
"""


print(printDash(xDic[secretId], ""))

setSecret(xDic[secretId],"")

while False:
	guess = str(input("guess a latter: "))
	print(printDash(xDic[secretId],guess))





print("len=",len(xDic),"secrrr",secretId)

print(xDic[3])

print(printDash(xDic[secretId],"a"))

"""
