import sys

tot = 0
N = int(sys.stdin.readline())
num = sys.stdin.readline()
for i in range(N):
    tot += int(num[i])

print(tot)
