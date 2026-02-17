import sys


# 깊이 우선 탐색 함수
def DFS(node):
    visited[node] = True

    for next_node in graph[node]:
        if not visited[next_node]:
            DFS(next_node)


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

# 인덱스가 컴퓨터 번호인 리스트, 인덱스 0은 미사용
graph = [[] for _ in range(N + 1)]

# 방문 여부를 저장할 graph와 같은 길이의 리스트
visited = [False] * (N + 1)

for _ in range(M):
    node_a, node_b = map(int, sys.stdin.readline().split())

    graph[node_a].append(node_b)
    graph[node_b].append(node_a)

DFS(1)

# 자기자신을 제외한 방문 횟수
print(sum(visited) - 1)
