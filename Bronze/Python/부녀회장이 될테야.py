import sys

# test case 입력받기
T = int(sys.stdin.readline())
k, n = [], []
for i in range(T):
    k.append(int(sys.stdin.readline()))
    n.append(int(sys.stdin.readline()))

# DP table 생성 및 초기화
residents = [[] for _ in range(15)]
for i in range(1, 15):
    residents[0].append(i)
    residents[i].append(1)

# DP table 채우기
for i in range(1, 15):
    for j in range(1, 14):
        residents[i].append(residents[i - 1][j] + residents[i][j - 1])

# DP table 검사
# for index, item in enumerate(residents):
#   print(f"{index}: {item}")

# 정답 출력
for i in range(T):
    print(residents[k[i]][n[i] - 1])
