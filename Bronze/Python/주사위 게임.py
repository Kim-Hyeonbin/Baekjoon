import sys

N = int(sys.stdin.readline())

res = 0
for _ in range(N):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == b and a == c:
        money = 10000 + a * 1000
    elif a == b or a == c:
        money = 1000 + a * 100
    elif b == c:
        money = 1000 + b * 100
    else:
        money = max((a, b, c)) * 100

    res = money if money > res else res

print(res)
