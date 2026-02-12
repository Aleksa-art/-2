def average(*args):
    return sum(args) / len(args) if args else 0

print(average(1, 2, 3, 4, 5))
