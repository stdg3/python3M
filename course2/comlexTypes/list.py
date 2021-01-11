# list: 
naoAList = (1,2,3,)
list1 = [1,2,3]
list2 = list(naoAList)

print("list2 = ", list2)
print(list1 == list2, list1 == naoAList)

# list operations:
# add:
# Note the difference between "append()" and "+=" for tuples.
list1.append(3)
print("append() returns None: ", list1.append(4))
print(list1)

list1.append(list2)
print("append l2 to l1 ",list1)

list1.extend(list2)
print("extend l2 from l1",list1)

list1.insert(1,"inserted")
print("inserted in l1",list1)

# List Are Mutable
var = ["bar"]
newVar = var
var.append("foo")
var[0]= "baz" #assign item
print("new var: ", newVar)

# delete:
testList = ["pop", "remove", "del"]

# by index:
popped = testList.pop(0)
print("popped value is '{}'".format(popped)) # sildiği değeri geri döndürür

# by value:
testList.remove("remove")

# or del il:
del testList[0] # del doesn't return a value
print(testList)

# multi-dimensional list:
multi = [
	[0,1,2,3,],
	[4,5,6,7,],
	[8,9,10,11,],
]#matrix 4*3

for row in multi:
	print(row)
	for element in row:
		print("element: ",element)

# generating list: range() function

print("range",range(0,10))

for i in list(range(1,15,2)):
	print(i)
