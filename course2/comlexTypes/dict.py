thisIsDict = {"key": "value"}
thisIsAlseDict = {"key":"value"}
print(thisIsDict == thisIsAlseDict)

var = {1:"value"}
newVar = var
var.update({2: "new value"})
var.update({1: "one"})
var[1] = "mutated value"
print("new var", newVar)

# operations witgh dicts:

# add:
thisIsDict.update({"name": "Super Mario"})
print("add: ", thisIsDict)

# get:
print("name is {}".format(thisIsDict["name"]))

print("name is {}".format(thisIsDict.get("name", 
	"default name"))
) #get'te aranan anahtar bulunmazsa mesela defName gibi sonuçta hata döndürmez prog çatlamaz None döner
print("keys:",thisIsDict.keys())
print("values:",thisIsDict.values())
print("len:",len(thisIsDict)) # keys kadar döner

for x in thisIsDict:
	print(x, thisIsDict[x])

for key, value in thisIsDict.items():
	print(key, value)

# remove:
testDict = {"popByKey": 1, "popItem": 2, "toDel":3}

del testDict["toDel"]
print(testDict)

popped = testDict.pop("popByKey")
print("popped: ",popped)

#missing = testDict.pop("noExistingKey")
#print("missing: ",missing)

popped=testDict.popitem()
print("poppeditem:",popped)

print("test dict", testDict)

# iterative:
toIterate = {1: "x2", 2: "x4", 3: "x8"}
for key in toIterate:
	print("key toIterate[key]",key, toIterate[key])

for key, value in toIterate.items():
	print("key values",key, value)

# clear:
toClear = {"key": "value", 1:2}
toClear.clear()
print("cleared ",toClear)

# string format:
print("{firstName}, {secondName}".format(
	secondName="Clark", 
	firstName="kent")
	)