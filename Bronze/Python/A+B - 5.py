import sys

for n in sys.stdin:
    A, B = map(int, n.split())

    if A == 0 and B == 0:
        break

    print(A + B)
