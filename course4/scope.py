def scopedVal(x):
	value = x +10
	print(value)

print(scopedVal, scopedVal(2))

#return someting

def returnSome(val):
	calc = val - 7
	return calc
print(returnSome, returnSome(4))

# global scope 
someVar = "Value"

def printVar():
	print(someVar)
printVar()
#print(someVar, printVar())

# you can not modify global scope
def modifyScope():
	try:
		someVar +="Extra"
	except UnboundLocalError as e:
		print("Error", e)

modifyScope()
print(someVar)

# but you can mutate it

globalList = []

def appendToList (item):
	print("adding...",item)
	globalList.append(item)

appendToList(2)
appendToList(5)
print(globalList)