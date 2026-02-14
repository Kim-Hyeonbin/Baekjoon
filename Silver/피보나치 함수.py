import sys

# 문제 범위 설정
N = 41

# DP 테이블 생성 및 채우기
dp_table = [[0 for _ in range(2)] for _ in range(N)]

dp_table[0][0] = 1
dp_table[1][1] = 1

for row in range(2, N):
    dp_table[row][0] = dp_table[row - 1][0] + dp_table[row - 2][0]
    dp_table[row][1] = dp_table[row - 1][1] + dp_table[row - 2][1]


# 입출력
T = int(sys.stdin.readline())

for _ in range(T):
    target = int(sys.stdin.readline())
    sys.stdout.write(" ".join(map(str, dp_table[target])) + "\n")
