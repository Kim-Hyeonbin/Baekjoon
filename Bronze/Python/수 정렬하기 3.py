import sys

N = int(sys.stdin.readline())

# 입력범위가 정해져 있으므로 계수 정렬 사용
count = [0 for _ in range(10001)]

for _ in range(N):
    x = int(sys.stdin.readline())
    count[x] += 1

for index, value in enumerate(count):
    for _ in range(value):
        sys.stdout.write((str(index) + "\n"))
