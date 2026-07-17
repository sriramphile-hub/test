n = int(input())

total_sum = 0
for i in range(1, n + 1):
    if i % 2 != 0:
        total_sum += i

print(f"Sum of Odd Numbers from 1 to {n}: {total_sum}")