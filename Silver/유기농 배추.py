import sys


# 가독성을 위해 BFS 함수 분리
def BFS(row, col):
    field[row][col] = 0

    queue = []
    queue.append((row, col))

    while queue:
        node = queue.pop(0)
        r, c = node[0], node[1]

        # 상하좌우 체크 후 BFS 큐에 추가
        if r != 0:
            if field[r - 1][c] == 1:
                field[r - 1][c] = 0
                queue.append((r - 1, c))
        if r != N - 1:
            if field[r + 1][c] == 1:
                field[r + 1][c] = 0
                queue.append((r + 1, c))
        if c != 0:
            if field[r][c - 1] == 1:
                field[r][c - 1] = 0
                queue.append((r, c - 1))
        if c != M - 1:
            if field[r][c + 1] == 1:
                field[r][c + 1] = 0
                queue.append((r, c + 1))


T = int(sys.stdin.readline())

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    count = 0

    # (M+1)*(N+1) 사이즈의 그래프 만들기 (0행과 0열은 미사용)
    field = [[0 for _ in range(M)] for _ in range(N)]

    # 그래프 채우기
    for _ in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        field[Y][X] = 1

    for row in range(len(field)):
        for col in range(len(field[row])):
            # 1이지만 아직 방문하지 않은 노드 탐색
            if field[row][col] == 1:
                count += 1

                # 너비 우선 탐색으로 연결된 유효 노드를 방문 처리 (1 -> 0)
                BFS(row, col)

    print(count)
