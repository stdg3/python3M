class Test:
	pass

class Test(object): # its the same as the code above (py3 only)
	pass 
#classes can inherit other classes

class Person(object):
	biologicalName = "homo sapiens"
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def walk (self):
		print("walking")
	def sayHello(self):
		print("im a person", self.name, self.age)

class Student(Person):
	def sayHello(self):
		print("im a student", self.name, self.age)

s = Student("inav", 22)	
print(s.biologicalName)
s.walk()
s.sayHello()

class Child(Person):
	def walk(self):
		raise ValueError("Can not walking")
	def sayHello(self):
		raise ValueError("Can not talk")
	def crawl(self):
		print("haha")
child = Child("steve", 1)
print(child.biologicalName)