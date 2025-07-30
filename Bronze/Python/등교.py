import sys

N, X = map(int, sys.stdin.readline().split())

bus = 0
for _ in range(N):
    S, T = map(int, sys.stdin.readline().split())
    if S + T <= X and S > bus:
        bus = S

print(bus if bus != 0 else -1)
