import sys

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    clothes = {}
    for _ in range(n):
        cloth, type = sys.stdin.readline().split()
        clothes[type] = clothes.get(type, 0) + 1

    answer = 1
    for count in clothes.values():
        answer *= count + 1

    # 완전 알몸인 경우 제외
    print(answer - 1)
