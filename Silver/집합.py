import sys

M = int(sys.stdin.readline())
S = 0

for _ in range(M):
    input_data = sys.stdin.readline().split()
    command = input_data[0]
    if len(input_data) > 1:
        x = int(input_data[1])

    if command == "add":
        S |= 1 << (x - 1)
    elif command == "remove":
        S &= ~(1 << (x - 1))
    elif command == "check":
        if S & (1 << (x - 1)):
            sys.stdout.write(str(1) + "\n")
        else:
            sys.stdout.write(str(0) + "\n")
    elif command == "toggle":
        S ^= 1 << (x - 1)
    elif command == "all":
        S = (1 << 20) - 1
    elif command == "empty":
        S = 0
    else:
        continue
