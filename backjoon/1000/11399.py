people = int(input())
times = list(map(int, input().split()))
times.sort()
total = 0
for time in times:
    total += time * people
    people -= 1
print(total)