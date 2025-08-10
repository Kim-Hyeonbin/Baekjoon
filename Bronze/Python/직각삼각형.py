import sys

while True:
    L = [int(n) for n in sys.stdin.readline().split()]

    if L[0] == L[1] == L[2] == 0:
        break

    max_num = max(L)
    L.remove(max_num)

    if max_num**2 == L[0] ** 2 + L[1] ** 2:
        print("right")
    else:
        print("wrong")
