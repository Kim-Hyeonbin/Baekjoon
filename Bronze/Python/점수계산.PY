import sys

N = int(sys.stdin.readline())
res = sys.stdin.readline().split()
score = 0
cnt = 1

for e in range(N):
    if res[e] == "1":
        score += cnt
        cnt += 1
    else:
        cnt = 1

print(score)
