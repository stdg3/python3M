# first:
myGlobalVar = 3

if myGlobalVar > 2:
	innerIfVar = "set"

print(innerIfVar)

if myGlobalVar != 3:
	thisWontHappen = "Nein!"
else:
	butThisWill = "Yes"

print(butThisWill)
#print(thisWontHappen)

# second:
var = 1
value = var
var = 10

# third:
var = "big string, very long. so memory usage."
other = var
del var

# fourth:
var = "string"
value = var
value += " is immutable"

# what can be stored insade a variable? everything!
strintInside = "abc"
intInside = 123
functionInside = len
boolInside = True
noneInside = None