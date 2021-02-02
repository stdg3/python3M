GLOBALVALUE = 2

def doWork(value):
	return GLOBALVALUE * value +2

def changeVar(x):
	global GLOBALVALUE
	GLOBALVALUE = x


class Calc:
	def __init__(self,param):
		self.param = param

	def doWork(self,value):
		return self.param * value + 2

	def changeVar (self,x):
		self.param = x