import sys

N = int(sys.stdin.readline())
title = 0

for i in range(N):
    title += 1
    while "666" not in str(title):
        title += 1

print(title)
