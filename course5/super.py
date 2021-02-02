class Parent:
	def printInfo(self):
		print("some info")

class SomeChild(Parent):
	def printInfo(self):
		super().printInfo()
		print("some other info")

s = SomeChild()
s.printInfo()