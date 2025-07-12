times = int(input())
words = [input().strip() for _ in range(times)]
words = sorted(set(words), key=lambda x: (len(x), x))
for word in words:
    print(word)