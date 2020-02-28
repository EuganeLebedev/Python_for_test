def likes(names):
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return names[0] + " likes this"
    elif len(names) <= 3:
        result = ''
        for name in names:
            if names.index(name) == len(names) - 1:
                result += 'and ' + name
            elif names.index(name) == len(names) -2:
                result += name + ' '
            else:
                result += name + ', '
        return result + " likes this"
    else:
        result = ''
        for name in names[:2]:
            if names.index(names) < 1:
                result += name + ", "
            else:
                result += name


        return result

names = ['Peter', 'John', 'Bob', 'Zoho', 'Zulu']
print(likes(names))