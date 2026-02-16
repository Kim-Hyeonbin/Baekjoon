MAX_N = 10**6 + 1

dp_table = [0 for _ in range(MAX_N)]
dp_table[1] = 0

for i in range(2, MAX_N):
    dp_table[i] = dp_table[i - 1] + 1
    if i % 2 == 0:
        dp_table[i] = min(dp_table[i], dp_table[i // 2] + 1)
    if i % 3 == 0:
        dp_table[i] = min(dp_table[i], dp_table[i // 3] + 1)

print(dp_table[int(input())])
