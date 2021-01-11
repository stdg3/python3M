simpleTuple = (1, 2, 4, 5)
print(simpleTuple)

# operations

# add
simpleTuple += (6,)

# tuples:
# Tuples are  IMMUTABLE!
emtyTuple = tuple() # show __built__
tuple1 = (1, ) # tek karakterli
tuple2 = (2,)
notATuple = (1) # this is not tuple!

print(
	tuple1 == tuple2, 
	tuple2 == notATuple, 
	type( notATuple)
	)
print((1,2) == (1,2))

# tuple operations:

# add:
tuple1 = tuple1 + tuple2
print(tuple1) 

tuple1 = (2, ) + tuple1 + (notATuple,)
print(tuple1)

# indexing:
print(1 in tuple1, 2 in tuple1)

print("len",len(tuple1),len(tuple2), len(emtyTuple))
print(tuple2[0], tuple1[0:2], tuple1[-1])

# removing:
# There is no direct way to delete an element from the tuple
tuple1 = (1, 3, "sting", "one more") 
print(tuple1)
newTuple = tuple()
for item in tuple1: # tıuple is itarable
	#we will remove all the "strings" frm tuple1
	#if not isinstance (item, (str, unicode)):
	if not isinstance(item, str):
		newTuple += (item, )
print(newTuple)

# nested:
print( ( 1, ("a", (tuple(), ), "b"), 2, ) )

# multiply:
print("multiply: ", tuple2 * 3)

# unpack:
var1, var2, _= ("foo", "bar", "_")
print(var2, var1)