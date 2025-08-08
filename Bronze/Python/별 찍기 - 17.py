N = int(input())
line_num = N
for n in range(1, N + 1):
    if n != N:
        for _ in range(line_num - 1):
            print(" ", end="")
        print("*", end="")
        line_num -= 1

        if n != 1:
            for _ in range(2 * (n - 2) + 1):
                print(" ", end="")
            print("*")
        else:
            print()
    else:
        for _ in range(n * 2 - 1):
            print("*", end="")
