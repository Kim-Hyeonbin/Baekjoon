import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

count = {}
for i in nums:
    count[i] = count.get(i, 0) + 1

M = int(sys.stdin.readline())
targets = list(map(int, sys.stdin.readline().split()))

res = []
for i in targets:
    res.append(str(count.get(i, 0)))

print(" ".join(res))
