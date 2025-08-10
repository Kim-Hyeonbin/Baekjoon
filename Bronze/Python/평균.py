import sys

N = int(sys.stdin.readline())
score_list = [int(n) for n in sys.stdin.readline().split()]
M = max(score_list)
fake_score_list = [s / M * 100 for s in score_list]

print(sum(fake_score_list) / N)
