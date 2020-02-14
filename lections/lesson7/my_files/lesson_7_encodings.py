s = 'qweqweqweqwe' # UTF-8
b = b"qweqweqweqwe" # byte

print(s)
print(b) #Будет декодировано и выведена строка

bs = s.encode()
ss = bs.decode()
ss = bs.decode('ascii')

