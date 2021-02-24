insType = type(14)
print(insType)
print("But what is insType's type?", type(insType))

# you can get class from instances
class Test(object):
    pass

t = Test()
print(t.__class__)

# simple example
print("instances are objects", isinstance(t,object))
print("classes are objects two!", isinstance(Test, object))

Test.some_value =12

#print(t.some.value)

#difference between class attributes and instance atributes
class DemoClass():
    classValue = "i belong to the class"

    def __init__(self, inst_value):
        self.inst_value = inst_value

d = DemoClass("abc")
d1 = DemoClass("zzz")

d1.inst_value = "xxx"
d1.classValue = "yyy"
print(d.inst_value , d1.inst_value)
print(d.classValue, d1. classValue)

DemoClass.classValue = "i am shared between all instances"
print(d.classValue, d1.classValue)