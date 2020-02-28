class MyDict:
    def __init__(self):
        pass

    # Переопределение getitem (Квадратные скобки при получении значения аттрибута)
    def __getitem__(self, item):
        return 11


d = MyDict()
item = d['asdasdasd']
print(item)
