import sys

L = list(map(int, sys.stdin.read().split()))
print(f"{max(L)}\n{L.index(max(L))+1}")
