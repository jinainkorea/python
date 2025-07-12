times = int(input())
schdules = []
for _ in range(times):
    start, end = map(int, input().split())
    schdules.append((start, end))
schdules.sort(key=lambda x: (x[1], x[0]))
count = 0
last_end = 0
for start, end in schdules:
    if start >= last_end:
        count += 1
        last_end = end

print(count)