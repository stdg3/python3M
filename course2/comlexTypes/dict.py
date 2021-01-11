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
print("len:",len(thisIsDict)) # key kadar döner

for x in thisIsDict:
	print(x, thisIsDict[x])

for key, value in thisIsDict.items():
	print(key, value)