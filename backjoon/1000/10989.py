import sys
input = sys.stdin.readline

times = int(input())

count = [0] * 10001

for _ in range(times): 
    count[int(input())] += 1

for i in range(10001):
    if count[i] > 0:
        for _ in range(count[i]):
            print(i)