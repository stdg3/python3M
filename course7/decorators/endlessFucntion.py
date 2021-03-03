def endlessFunction():
    print("i am endless")
    return endlessFunction

endlessFunction()()()()()()()()

x = endlessFunction()
print(x , x == endlessFunction)