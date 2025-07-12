times = int(input())
x = []
y = []
for _ in range(times):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)
points = sorted(zip(x, y), key=lambda p: (p[1], p[0]))
for point in points:
    print(point[0], point[1])