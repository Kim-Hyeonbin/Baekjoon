import sys
from math import comb

T = int(sys.stdin.readline())
res = []

for _ in range(T):
    r, n = map(int, sys.stdin.readline().split())
    res.append(comb(n, r))

for e in res:
    print(e)
