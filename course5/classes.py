class Car:
	pass
c = Car()
print("print car() and type(car())",c, type(c))

# Classes can have variables called fields

class Room:
	number = "Room 34"
	floor = 4

r = Room()
r1 = Room()

print("room number",r.number, r1.number)
print("room's floor",r.floor, r1.floor)

# you can modifies values:
r.number = 12
r.floor = "5 floor"
print("room number",r.number, r1.number)
print("room's floor",r.floor, r1.floor)

# Classes can have functions inside:

class Door:
	def open(self): # note that "self" is the object
		print("self", self)
		print("door is opened!")
		self.opened = True

d = Door()
d.open()

# method vs function farkı 
# method clasın içinde ve self barındırıyor
# function def ile tanımladığımız

class Terminal:
	def sayHello(self, user):
		print("self is the object itself", self)
		print("Hello",user)
t = Terminal()
t.sayHello("Python")

# classes can have both methods and fields

class Window:
	isOpened = False

	def open(self):
		self.isOpened = not self.isOpened
		print("Window is now", self.isOpened)

w = Window()
w1 = Window()
print("Initial state", w.isOpened,w1.isOpened)
w.open()
print("New state", w.isOpened,w1.isOpened)

