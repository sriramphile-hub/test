n = int(input())
m = int(input())

result = []
current_number = n

while current_number >= 0:
    result.append(current_number)
    current_number -= m

print(*result)