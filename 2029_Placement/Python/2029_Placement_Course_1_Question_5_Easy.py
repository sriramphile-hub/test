num = int(input())
result = []
for i in range(1, num + 1):
    if i % 5 != 0 and i % 7 != 0:
        result.append(str(i))
print(" ".join(result))