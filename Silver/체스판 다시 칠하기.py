import sys

# N은 행, M은 열
N, M = map(int, sys.stdin.readline().split())
chessboard = []
for _ in range(N):
    chessboard.append(sys.stdin.readline().rstrip())

min_change = 65

# 8x8 구조가 가능한 범위내에서 반복
for i in range(N - 7):
    for j in range(M - 7):
        # 8x8 구조에서 행과 열을 검사
        count_b = 0
        count_w = 0
        for row in range(i, i + 8):
            for col in range(j, j + 8):

                # 좌표 합이 짝수일 때 타일 색
                if (row + col) % 2 == 0:
                    if chessboard[row][col] == "W":
                        count_b += 1
                    if chessboard[row][col] == "B":
                        count_w += 1

                # 좌표 합이 홀수일 때 타일 색
                else:
                    if chessboard[row][col] == "B":
                        count_b += 1
                    if chessboard[row][col] == "W":
                        count_w += 1

        min_change = min(min_change, count_b, count_w)

print(min_change)
