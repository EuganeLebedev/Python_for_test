class MyDict:
    def __init__(self):
        pass

    def __getitem__(self, item):
        return 11


d = MyDict()
item = d["asdasd"]
print(item)
