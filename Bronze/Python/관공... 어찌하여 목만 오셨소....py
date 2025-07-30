import sys

N = int(sys.stdin.readline())

for _ in range(N):
    string = sys.stdin.readline()
    if "S" in string:
        print(string)
