import sys

N = int(sys.stdin.readline())
stack = []

for _ in range(N):
    command = sys.stdin.readline().strip()

    if command[:4] == "push":
        stack.append(int(command[5:]))
    elif command == "top":
        print(stack[-1] if len(stack) > 0 else -1)
    elif command == "size":
        print(len(stack))
    elif command == "empty":
        print(1 if len(stack) == 0 else 0)
    elif command == "pop":
        print(stack.pop() if len(stack) > 0 else -1)
