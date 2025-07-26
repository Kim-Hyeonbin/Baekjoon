import sys

N = int(sys.stdin.readline())

for i in range(N):
    for j in range(i):
        print(" ", end="")
    for j in range(2 * N - (2 * i + 1)):
        print("*", end="")
    print()
