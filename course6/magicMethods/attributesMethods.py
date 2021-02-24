class AtttibutesClass(object):
    def __init__(self, values):
        super(AtttibutesClass, self).__setattr__("values", values)
    
    def __getattr__(self, item):
        return self.vales[item]
    def __setattr__(self, key, values):
        self.values[key] = values
    
if __name__ == "__main__":
    attr = AtttibutesClass({"one": 1, "two": 2})
    attr.three = 3
    print(attr.three, attr.one)