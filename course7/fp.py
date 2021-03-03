def work(value):
    return value * 2

t = [1, 3, 8]
m = map(work, t) # her t için worku çağırır
print(m)
print(list(m))

# the same, bey using lambda function
m1 = map(lambda x: x * 2, t)
print(list(m1))

#filter
print(list(filter(lambda v: v > 0, [-1, -5, 20, 3, 0])))

# reduce 
from functools import reduce

r = [1, 4, 5, 3]

result = reduce(lambda x, y: x + y, r)
print(result)