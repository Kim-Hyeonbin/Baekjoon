import sys

T = int(sys.stdin.readline())

for _ in range(T):
    line = sys.stdin.readline()
    digit, text = int(line.split()[0]), line.split()[1]
    for i in text:
        print(i * digit, end="")
    print()
