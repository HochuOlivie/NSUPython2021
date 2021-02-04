arr = []
result = [0]
for i in input().split():
    arr.append(int(i))
    result.append(sum(arr))
print(result)
