import sys

N = int(sys.stdin.readline())
nums = set(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
targets = list(map(int, sys.stdin.readline().split()))

for i in targets:
    print(1 if i in nums else 0)
