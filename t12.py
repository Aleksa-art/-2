names = [name for name in ["Нейтан", "Біл", "Ніка", "Бонні"]]

def name_length(name):
    return len(name)

nameDict = {name: name_length(name) for name in names}

nameDict = dict(sorted(nameDict.items(), key=lambda item: item[1]))

print(nameDict)
