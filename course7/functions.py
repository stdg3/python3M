def long(value):
    import time
    time.sleep(5) #delays for 5 seconds

    return "long" + str(value)

def short(string_param):
    print("speed:", string_param)
    return "short"

def medium(value, *modificators):
    result = value
    for m in modificators:
        result *=modificators
    
    return result

def shange_sim(num, check_sing=True):
    if check_sing and num > 0:
        raise ValueError("num > 0!")
    return -num