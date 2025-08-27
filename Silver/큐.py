import sys

N = int(sys.stdin.readline())
queue = []

for _ in range(N):
    command = sys.stdin.readline().strip()

    if "push" in command:
        queue.append(int(command.split()[1]))

    elif command == "size":
        print(len(queue))

    elif command == "empty":
        print(1 if len(queue) < 1 else 0)

    elif command == "pop":
        if queue:
            print(queue[0])
            queue[0:] = queue[1:]
        else:
            print(-1)

    elif command == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)

    elif command == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)
