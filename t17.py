list1 = ["a", "b"]
list2 = [1, 2, 3]

combinations = []

for item1 in list1:
    for item2 in list2:
        combinations.append((item1, item2))

print(combinations)
