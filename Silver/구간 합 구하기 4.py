import sys

N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
sums = [0]

for num in nums:
    sums.append(num + sums[-1])

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    print(sums[j] - sums[i - 1])
