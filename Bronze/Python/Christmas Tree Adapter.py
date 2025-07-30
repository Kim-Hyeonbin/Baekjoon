import sys

a = int(sys.stdin.readline())
w, v = map(int, sys.stdin.readline().split())

print(1 if a <= (w / v) else 0)
