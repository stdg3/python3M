# we can expland list and dicts

def acceptArgs (*args):
	print(args)
	return sum(args)

print(acceptArgs (1,2,5,4,6,8))

values = [2,5,4,6]

try :
	acceptArgs(values)
except TypeError as e:
	print(e)

print(acceptArgs(*values))

#kwargs is the same

def acceptKwargs (**kwargs):
	print(kwargs)

acceptKwargs(name="Python", version = 3)

values = {"day": "wed", "month": 3}

try:
	acceptKwargs(values)
except Exception as e:
	print("error:", e)

acceptKwargs(**values)