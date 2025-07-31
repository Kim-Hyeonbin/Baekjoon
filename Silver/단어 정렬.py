import sys

N = int(sys.stdin.readline())
words = {sys.stdin.readline().strip() for _ in range(N)}
for e in sorted(sorted(list(words)), key=len):
    print(e)
