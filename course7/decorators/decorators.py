def actionDecorator(func):
    def inner(text):
        print("some is going to", func.__name__)
        func(text)
    return inner

@actionDecorator
def shout(text):
    print(text.upper(), "!!!")

@actionDecorator
def whisper(text):
    print(text.lower(), "...")

@actionDecorator
def say(something):
    something += "; was said."
    print(something)

if __name__=="__main__":
    say("hi")
    whisper("hello")
    shout("i am here")