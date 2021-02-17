class TestClass:
	def __init__(self): #const ifadesi
		print("Constructor is called")
		print("self is the object itself",self)

t = TestClass()
t1 = TestClass()

# constructor can have parameters

class Table:
	def __init__(self, numberOfLegs):
		print("new table has {} legs".
			format(numberOfLegs))

t = Table(4)
t1 = Table(3)


# but we need to save them into the fields

class Chair:
	def __init__(self, color):
		self.color = color

c = Chair("green")
print(c, c.color)

c1 = Chair("red")
print(c1.color)
print("variable c did not change!", c.color)
# позиционный именованный аргс кваргс 
