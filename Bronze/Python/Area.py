import sys

n = int(sys.stdin.readline())

h = []
w = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    h.append(a)
    w.append(b)

area = [h[i] * w[i] for i in range(n)]

print(max(area))
