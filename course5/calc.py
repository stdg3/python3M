class Calc(object):
	def __init__(self, number):
		self.number = number

	def calcAndPrint(self):
		value = self.calcValue()
		self.printNumber(value)

	def calcValue(self):
		return self.number * 10 + 2

	def printNumber(self, value):
		print("-" * 10)
		print("Number is", value)
		print("-" * 10)

class CalcExtraVal(Calc):
	def calcValue(self):
		return self.number * 100

c = Calc(4)
c.calcAndPrint()
c1 = CalcExtraVal(4)
c1.calcAndPrint()

