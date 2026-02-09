import sys

number_of_test_case = int(sys.stdin.readline())

for _ in range(number_of_test_case):

    # N은 문서 개수, M은 몇 번째로 출력되는지 궁금한 문서의 위치
    N, M = map(int, sys.stdin.readline().split())
    importances = list(map(int, sys.stdin.readline().split()))
    cnt = 0

    while True:
        # M을 가변 인덱스로 다루어 문서를 실시간 추적하게 함
        if importances[0] == max(importances):
            cnt += 1
            if M == 0:
                break
            importances.pop(0)
            M -= 1
        else:
            if M == 0:
                M = len(importances) - 1
            else:
                M -= 1
            importances.append(importances.pop(0))

    sys.stdout.write(str(cnt) + "\n")
