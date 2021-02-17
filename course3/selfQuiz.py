import random

def randExcept(x):
	try:
		if x == 1:
			raise TypeError("xxxtypeError")
		elif x == 2:
			raise RuntimeError("xxxRuntime")
		elif x == 3:
			raise ValueError("xxxValError") 	
	except TypeError as e:
		print("[1]random", e)
	except RuntimeError as e:
		print("[2]random",e)
	except ValueError as e:
		print("[3]random",e)

def sortInt(*args):
	try:
		flag = bool()
		for x in args:
			if isinstance(x, int):
				flag = True
			else:
				flag = False
				break
		if flag == True:
			l = list()
			#l.sort()
			for x in args:
				l.append(x)
			#args.sort()
			l.sort()
			print(l)
		elif flag == False:
			raise ValueError("sort only int")
	except ValueError as e:
		print(e)

def dictToStr(**kwargs):
	print(kwargs)
	for x, y in kwargs.items():
		#z = ""
		#z +=str(y)
		kwargs.update({x: str(y)})
		#print(x, type(z), type(y))
	return kwargs


def multiplication(*n):
	res = 1
	for x in n:
		res *= x
	return res


sortInt(2,4,1,)
sortInt(2,5,"asd")
randExcept(random.randint(1,3))
print(dictToStr(c=1, b=2, a=3))
print(multiplication(2,4))
