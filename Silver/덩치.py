import sys

N = int(sys.stdin.readline())

students = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

ranks = []

for i in range(N):
    rank = 1
    for j in range(N):
        if i != j:
            if students[j][0] > students[i][0] and students[j][1] > students[i][1]:
                rank += 1
    ranks.append(rank)

print(*ranks)
