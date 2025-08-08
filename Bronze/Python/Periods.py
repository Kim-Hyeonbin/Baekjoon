import sys

N = int(sys.stdin.readline())

for _ in range(N):
    sentence = sys.stdin.readline().strip()
    if sentence[-1] != ".":
        sentence += "."
    print(sentence)
