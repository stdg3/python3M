from normalPackage.normalFile import MyClass, myFunction, GlobalVar

myFunction()

try:
    from notAPackage.myModule import printInfo

    printInfo()
except ImportError as e:
    print(e)