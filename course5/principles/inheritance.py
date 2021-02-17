class Parent(object):
	def __init__(self):
		print("parent inited")
		self.value = "parent"

	def do(self):
		print("parent do(): {}".format(self.value))

class Child(Parent):
	def __init__(self):
		print("child inited")
		self.value = "child"

parent = Parent()
parent.do()

child = Child()
child.do()