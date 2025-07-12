input = input().split('-')
input = [sum(map(int, i.split('+'))) for i in input]
result = input[0]
for i in input[1:]:
    result -= i
print(result)