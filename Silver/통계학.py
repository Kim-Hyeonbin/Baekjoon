import sys

N = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for _ in range(N)]

# 산술평균
mean = sum(numbers) / len(numbers)
print(int(mean + 0.5) if mean >= 0 else int(mean - 0.5))

# 중앙값
print(sorted(numbers)[len(numbers) // 2])

# 최빈값 (배열 카운팅을 통해 풀이)
count = [0 for _ in range(8001)]
for num in numbers:
    count[num + 4000] += 1
max_count = max(count)
flag = False

for idx, cnt in enumerate(count):
    if flag and cnt == max_count:
        mode = idx - 4000
        break
    if cnt == max_count:
        mode = idx - 4000
        flag = True
print(mode)


# 범위
print(max(numbers) - min(numbers))
