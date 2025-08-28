import sys

n = int(sys.stdin.readline())

if n != 0:
    difficulty = []
    for _ in range(n):
        difficulty.append(int(sys.stdin.readline()))
    difficulty.sort()

    # 사사오입 반올림
    exception = int(n * 0.15 + 0.5)
    if exception != 0:
        difficulty = difficulty[exception:-exception]

    print(int(sum(difficulty) / len(difficulty) + 0.5))
else:
    print(0)
