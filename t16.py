import math

points = [(1, 2), (3, 4), (0, 5)]
distances = {}

for point in points:
    x, y = point
    distances[point] = round(math.sqrt(x**2 + y**2), 2)

print(distances)
