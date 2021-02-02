class Parent():
 	def call(self):
 		print("parent")

class Child(Parent):
 	def call(self):
 		print("Child")

class Example():
 	def call(self):
 		print("ex")

def callObj(obj):
 	obj.call()

callObj(Child())
Child.call("asd")
callObj(Parent())