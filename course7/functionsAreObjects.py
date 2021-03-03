def myFunction():
    print("i am a function")

print("functions are objects", isinstance(myFunction, object))

# you can use var to store funtions
test = myFunction
test()

# you can pass functions as parameters

def callPassedFunction(incomming):
    print("calling")
    incomming()
    print("called")

callPassedFunction(myFunction)

# you can not call uncallable things

try:
    d = 2 
    d()
except TypeError as e:
    print("it is not a function", e)

# you can check if something could be called

print(callable(len), callable(45), callable(callable))

# you can return function from a function

def returnMinFunction():
    return min

test = returnMinFunction()
minvalue = test(4, 5, 8 ,0)
print("min val is: ", minvalue)