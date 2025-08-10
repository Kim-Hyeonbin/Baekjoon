import sys

N = int(sys.stdin.readline())
L = [int(n) for n in sys.stdin.readline().split()]
T, P = map(int, sys.stdin.readline().split())

T_total = 0

for e in L:
    T_total += e // T
    if e % T != 0:
        T_total += 1

print(T_total)
print(f"{N//P} {N%P}")
