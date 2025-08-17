import sys

N = int(sys.stdin.readline())
times = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
time_max = 0  # 최대 시간을 저장할 변수

for i in range(N):
    cover = [0] * 1000  # 근무 시간 마킹용 리스트
    for j in range(0, i):
        for k in range(times[j][0], times[j][1]):
            cover[k] = 1
    for j in range(i + 1, len(times)):
        for k in range(times[j][0], times[j][1]):
            cover[k] = 1

    time_max = max(cover.count(1), time_max)


print(time_max)
