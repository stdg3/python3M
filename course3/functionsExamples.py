# Here we define a function:
def printStars():
	print("*" * 20)

printStars()

# Step1:
def myFunc(input1, input2):
 	return input1 + input2

print("ret i1 + i2", myFunc(3,5))
print("second cals", myFunc(5,6))

# Step2:
printStars()

def myFuncPrint3Val(val1, val2, val3):
	print("No way I'm using this: {}, {}, {}".format(
		val1, val2, val3
		))
myFuncPrint3Val("v1", "v2", "v3")
print(myFuncPrint3Val("v1", "v2", "v3")) # return if olmadığından None ama içinde 1 kez ekrana basar

printStars()

# step 3
def myFuncWithDefVal(name, age=0, stars=False):
	print("{} is {} years old!".format(name, age))
	if stars:
		print("*" *5 )
myFuncWithDefVal("Python")
myFuncWithDefVal("Python", 20)
myFuncWithDefVal("Python", stars = True, age = 20)

# step4:
def namedVal(name=None, surname = None, patronimic = None):
	print("Full name: {name} {surn} {patrmc}".format(
		name=name, 
		surn=surname, 
		patrmc=patronimic
		))
namedVal(name="a", surname="v", patronimic="V")
namedVal(surname = "v", name="s", patronimic = "vv")


# complex sample: 
def sumAll(*args): # sınırsız veri alır 256 ;)
	print(args, type(args)) #tuple
	result = 0
	for x in args:
		result += x
	return result
print("sum all:",sumAll(1,2,3,4,6,4,4,))

# complex step2:
def factorial(n):
	if n == 0:
		return 1
	return n * factorial(n-1)
print("factorial 4= ",factorial(4))

# complex step3:
def doCallback(function, argument):
	return function(argument)

result = doCallback(len, "string")
print(result)

# complex step4:
def anyKeywargs(**kwargs):#dict oluşturuyor	
#default değerli any keywargs genel adı kwargs
	print(kwargs,type(kwargs))
anyKeywargs(a=1, qwe= 2, zzzz=4)

def all_together(value, *args, **kwargs):
    message = kwargs.pop('message', 'default message')
    if value > sum(args):
        print(message)
    else:
        print('value is not bigger than sum(args)')

all_together(1, 0)
all_together(1, 2, 3, 4)
all_together(5, 1, 1, 2, message='Done!')

# complex step 6:
def decorator(function):
	def _inner(value):
		print(function(value))
	print("called")
	return _inner

decorated = decorator(len)
decorated([1, 2, 4, 5,])