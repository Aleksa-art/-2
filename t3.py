limit = 101
listDelThree = []
for i in range(limit):
    if i == 0 or i % 3 != 0:
        continue
    elif i % 3 == 0:
        listDelThree.append(i)

print(listDelThree)
