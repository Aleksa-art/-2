matrix = []

for i in range(5):
    row = []
    for j in range(5):
        row.append(i * j)
    matrix.append(row)

for row in matrix:
    print(row)
