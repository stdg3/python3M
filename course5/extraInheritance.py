class Milk(object):
	def __init__(self, fat):
		self.fat = fat
	def taste(self):
		print("It tasted good.")
milk = Milk(3.5)
milk.taste()

class Cheese(Milk):
	def eat(self):
		print("Yammy")

	def taste(self, x):
		print("taste is",x)

russian = Cheese(30)
russian.taste("good")
russian.eat()

class C:
	difficulty = 10
class Python(C):
	difficulty = 2
class CPP(C):
	difficulty = 20
class Pyston(Python):
	difficulty =6