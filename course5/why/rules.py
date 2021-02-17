def mainFunc(obj):
	param = 34
	return obj.doSomething(param)

class SomeOldLogic:
	def doSomething(self, value):
		x = self.calc(value)
		print("x is calculated", x)

		print("a lot of work is done here")

		x += 44
		if x<0:
			x = 0
		x = x * 1.2

		return x

	def calc(self,value):
		return value * 7 +90

x = SomeOldLogic()
mainFunc(x)

class NewLogic(SomeOldLogic):
	def calc(self, value):
		return value -2

y = NewLogic()
mainFunc(y)
