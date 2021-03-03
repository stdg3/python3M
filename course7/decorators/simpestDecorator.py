def logger(function):
    def inner(x, y):
        result = function(x,y)
        print("res: ",result)
        return result
    return inner

def sum(x,y):
    return x + y

def mult(x,y):
    return x* y

s = logger(sum)
sResult= s(5,6)
print(sResult)

m = logger(mult)
mResult= m(5,6)
print(mResult)