def myFunc():
	print("I'm a function")

def rr():
	return "rr"

print(myFunc) # ()'siz olunca ramde adresi verir'
print("functions are object", isinstance(myFunc, object))

# you can use var to store func

test = myFunc
print("test:",test) # ramde adresi verir
print("test()", test())# testi çağırır yapar döndüsünde de return olmadığı için none verir
test()

# you can do any actions with funtions


myList = []
myList.append(rr())
myList.append(myFunc)
print("my list:",myList)

# you can pass function as parametrs

def callPassedFunc(incomming):
	print("Calling!")
	incomming()
	print("Called!")

callPassedFunc(myFunc)

# you can call uncallable things:

try:
	d = 2
	d()
except TypeError as e:
	print("it is not a function", e)

# you can check if something could be called
print ("callable :",callable(len), callable(45), callable(callable))

#you can return function from a function

def returnMinFunc():
	return min

test = returnMinFunc()
minVal = test(4, 5, -9, 12)
print("min val is :", minVal)

def returnMinFunc():
	