high = int(input())
low = int(input())
num = int(input())

for i in range(high, low - 1, -1):
    if i != num:
        print(i, end=" ")

print()