# fınction can use global variables

globalVar = 3

def usingGlobalVar(x):
	print(x * globalVar)

usingGlobalVar(2)

# but if we want to write to it, wq should state it expacitly

def writingToGlobalVar(val):
	global globalVar
	xGlobalVar = val
	print("it is now:",globalVar)

writingToGlobalVar(5)
print(globalVar)

# functions are objects and can be nested

def outherFunc(value):
	def someInner():
		print("print from inner! value was,", value)
	return someInner
v = outherFunc("some")
print("it is a func,", v, callable(v))
v() # some will be printed
